from datetime import timedelta, datetime, timezone
from restapi.models import Event, Reservable, Disponibilite, TypeDispo

__author__ = 'chassotce'

# Return freetime from a list of disponibilite and occupation
def getDispo(dispo,occupation):
    sd = []
    for d in dispo:
        sd.append(d)
        for o in occupation:
            o.start = o.start.astimezone(timezone.utc).replace(tzinfo=None)
            o.end = o.end.astimezone(timezone.utc).replace(tzinfo=None)
            for a in sd:
                # 1
                if (o.start <= a.start and o.end <= a.start) or (o.start > a.end):
                    pass
                #2
                if (o.start <= a.start and o.end >= a.end):
                    sd.remove(a)
                    break
                #3
                if (o.start < a.start and (o.end > a.start and o.end <a.end)):
                    a.start = o.end
                    pass
                #4
                if (o.start >= a.start and o.end<a.end):
                    if (o.start == a.start):
                        a.start=o.end
                        if(a.start == a.end):
                            sd.remove(a)
                    else:
                        if(o.end != a.end):
                            b = Event(start=o.end,end=a.end)
                            sd.append(b)
                            a.end = o.start

                    pass
                #5
                if (o.start >= d.start and o.start < d.end) and (o.end>d.end):
                    a.end = o.start
                    pass
    return sd


# Return the same free time between two list of event
def getSimilarDispo(dispo1,dispo2):
    sd = []
    if(not dispo1 or not dispo2):
        return []

    for d in dispo1:
        for o in dispo2:
            # 1
            if (o.start < d.start and o.end <= d.end) or (o.start > d.end):
                pass
            #2
            if (o.start < d.start and o.end > d.end):
                sd.append(d)
                pass
            #3
            if (o.start < d.start and (o.end > d.start and o.end <d.end)):
                b = Event(start=d.start,end=o.end)
                sd.append(b)
                pass
            #4
            if (o.start >= d.start and o.end<=d.end):
                b = Event(start=o.start,end=o.end)
                sd.append(b)
                pass
            #5
            if (o.start >= d.start and o.start < d.end) and (o.end>d.end):
                b = Event(start=o.start,end=d.end)
                sd.append(b)
                pass
    return sd


# Return the duration in minute of the event
def getTimeInEvent(event):
    delta = event.end - event.start
    return delta.seconds/60

# Return all area with the same duration with 5 minutes interval
def getAllArea(dispo,duration):
    dispos = []
    for e in dispo:
        if(getTimeInEvent(e)>= duration):
            z = Event()
            z.start = e.start
            z.end = z.start + timedelta(minutes=duration)
            dispos.append(z)
            delta = 5
            inc = 5
            while((e.end - timedelta(minutes=duration))> (z.start)):
                z = Event()
                z.start = e.start + timedelta(minutes=inc)
                z.end = z.start + timedelta(minutes=duration)
                dispos.append(z)
                inc += delta
    return dispos

# Save a prereservation
def reserveEvent(dispo,duration,session,ressource,prestation,activite):
    e = Event()
    e.session = session
    e.ressource = ressource
    e.type = "OCCUPE"
    e.state = "WAITING"
    e.start = dispo.start
    e.end = e.start + timedelta(seconds=duration*60)
    e.prestataire = ressource.prestataire
    e.prestation = prestation
    e.activity = activite
    e.save()
    return e

# Return the free time of a ressource
def getRessourceDispo(ressource,date):
    day = date.strftime("%a").upper()[0:2]
    dispo = Event.objects.filter(rule=day).filter(ressource=ressource).order_by("start")
    occupation = Event.objects.filter(start__contains=date.strftime("%Y-%m-%d")).filter(ressource=ressource).exclude(type="DISPONIBLE").order_by("start")
    for d in dispo:
            d.start = datetime.combine(date.date(),d.start.time())
            d.end = datetime.combine(date.date(),d.end.time())
    return getDispo(dispo,occupation)

# Return the event to reserve a date with a prestation
def prestationDispos(date,prestation,session,ressources=None):
    reserv = Reservable()
    for a in prestation.activitys.all():
        activitys = []
        for t in a.types.all():
            types = []
            for r in t.ressources.all():
                d = getRessourceDispo(r,date)
                ok = False
                for e in d:
                    if(getTimeInEvent(e)>=a.duration):
                        ok = True
                        break
                if(ok):
                    types.append(r)
            if(types):
                activitys.append(types)
        if(activitys.__len__()!=list(a.types.all()).__len__()):
            return reserv
        for i in activitys[0]:
            d = getRessourceDispo(i,date)
            d = getAllArea(d,a.duration)
            for e in d:
                if(getTimeInEvent(e)>=a.duration):
                    reserv.event = reserveEvent(e,a.duration,session,i,prestation,a)
                    ok = False
                    if(activitys.__len__() == 1):
                        ok = True
                    for n in range(1,activitys.__len__()):
                        ok = False
                        for t in activitys[n]:
                            if(ok):break
                            s = getSimilarDispo(getRessourceDispo(t,date),[reserv.event,])
                            for ax in s:
                                if(getTimeInEvent(ax)==getTimeInEvent(reserv.event)):
                                    ok = True
                                    reserveEvent(ax,a.duration,session,t,prestation,a)
                                    break
                        if(not ok):
                            Event.objects.filter(session=session).delete()
                            break
                    if(ok):return reserv
    return Reservable()

# Return types with ressources who are selectable
def getSelectableRessources(date,prestation,session,ressources=None):
    Event.objects.deleteOld()
    types = []
    typesdispos = Disponibilite()

    for a in prestation.activitys.all():
        for t in a.types.all():
            if(t not in types and t.isSelectable):
                typedispo = TypeDispo()
                typedispo.name = t.name
                typedispo.ressources = t.ressources
                typesdispos.typeDispo.append(typedispo)
                types.append(t)
    typesdispos.event = prestationDispos(date,prestation,session,ressources).event
    return typesdispos

# Get one event if two events are successive
# TODO doesn't work
def getContinuEvent(events):
    ce = []
    for e in events:
        a = Event(start=e.start,end=e.end)
        for i in events:
            if (i is a):
                pass
            if (i.start<a.start):
                pass
            if (i.start<a.end and i.end > a.end):
                a.end = i.end
            break
        ce.append(a)
        pass
    return ce