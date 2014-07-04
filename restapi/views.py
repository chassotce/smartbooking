from dateutil.parser import parse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.datetime_safe import datetime
from rest_framework import permissions, status
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from restapi.models import Prestataire,Type,Activite,Prestation,Client,Ressource,Event,Authentication,EVENT_TYPE,Type_Activite
from restapi.permissions import IsOwnerOrReadOnly
from restapi.serializers import PrestataireSerializer,TypeSerializer,ActiviteSerializer,PrestationSerializer\
    ,ClientSerializer,EventSerializer,RessourceSerializer,PasswordSerializer,AuthenticationSerializer,HoraireSerializer\
    ,CongeSerializer,DispoSerializer,Type_ActiviteSerializer,SelectableRessourceSerializer
from dateutil.rrule import *
from django.db.models import Q

class AuthenticationViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Authentication.objects.all()
    serializer_class = AuthenticationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PrestataireViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Prestataire.objects.all()
    serializer_class = PrestataireSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ActiviteViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PrestationViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ClientViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RessourceViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer
    permission_classes = (permissions.AllowAny,)

    def pre_save(self, obj):
        obj.user_id = 1
        obj.set_ressource = None

    @action()
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.DATA)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class EventViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HoraireViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Event.objects.filter(type='DISPONIBLE').order_by('start')
    serializer_class = HoraireSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.type = 'DISPONIBLE'
        obj.state = 'CONFIRMED'

    def post_save(self, obj, created=False):
        if(obj.ressources.count() == 0):
            obj.ressources.clear()
            obj.ressources.add(Ressource.objects.get(user=User.objects.get(username=self.request.user).id))
            obj.save()

class CongeViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Event.objects.filter(type='CONGE').order_by('start')
    serializer_class = CongeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.type = 'CONGE'
        obj.state = 'CONFIRMED'

    def post_save(self, obj, created=False):
        if(obj.ressources.count() == 0):
            obj.ressources.clear()
            obj.ressources.add(Ressource.objects.get(user=User.objects.get(username=self.request.user).id))
            obj.save()

class Type_ActiviteViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Type_Activite.objects.all()
    serializer_class = Type_ActiviteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DispoViewSet(viewsets.ViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the hightlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Event.objects.filter(type='CONGE').order_by('start')
    serializer_class = CongeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request):
        #
        #print(self.request.QUERY_PARAMS.get('date'))
        #print(self.request.QUERY_PARAMS.get('key'))
        #s = Event.objects.exclude(rule='')
        #day = parse(request.QUERY_PARAMS.get('date')).strftime("%a").upper()[0:2]
        #s = Event.objects.filter(rule=day)
        #for e in s:
        #    print(e.rule+" "+e.ressources.all().first().name)
        #    events = Event.objects.filter(Q(rule=day)|Q(start=request.QUERY_PARAMS.get('date'))).filter(ressources= e.ressources.all().first()).order_by("start")
        #    for ev in events:
        #        print(ev.start.strftime("%Y-%m-%d %H:%M:%S")+" "+ev.end.strftime("%Y-%m-%d %H:%M:%S") +" youyou")
        #        print(ev.start.strftime("%Y-%m-%d %H:%M:%S")+ " "+ str((ev.end - ev.start).total_seconds()))
        #        print("----------------------------------------------------------------------------------------")
        dispos=[]
        dispo = prestationDispos(parse(request.QUERY_PARAMS.get('date')))
        dispos.append(dispo)
        for ressource in Ressource.objects.all():
            r = None
            #r = freeTime(parse(request.QUERY_PARAMS.get('date')),ressource)
            #dispos.append(r)
            print(r)
        #dispos = getRessourcesDispo(Ressource.objects.all(),[],[],parse(request.QUERY_PARAMS.get('date')))
            #for e in r:
            #    dispo=None
            #    dispo = {'ressource':e.ressource,'area':e.area}
            #    dispos.append(dispo)
            #    for t in e.area:
            #        print(t.start.strftime("%Y-%m-%d %H:%M:%S")+" "+t.end.strftime("%Y-%m-%d %H:%M:%S")+" "+e.ressource.name)
        #queryset = [{'start':'2014-08-06 10:55:00',},{'start':'2014-08-06 10:55:00','start':'2014-08-06 10:55:00','start':'2014-08-06 10:55:00','start':'2014-08-06 10:55:00'}]
        #print(datetime.now().date())
        #t = '2014-08-06 10:55:00'
        #print(timezone.localtime(timezone.now()))
        #tc = datetime.now().strftime("%Y-%m-%d")+" "+ t.split(' ')[1]
        #for d in list(rrule(DAILY, byweekday=(MO),count=100,dtstart=parse(tc),)):
        #    print(d)

        #queryset=prestationDispos(parse(request.QUERY_PARAMS.get('date')))
        #serializer = DispoSerializer(queryset)
        queryset=getSelectableRessources(Prestation.objects.filter(id=int(request.QUERY_PARAMS.get('prestation'))).first())
        serializer = SelectableRessourceSerializer(queryset)

        return Response(serializer.data)

#def freeTime(date,ressource):
#    day = date.strftime("%a").upper()[0:2]
#    dispo = Event.objects.filter(rule=day).filter(ressources=ressource).order_by("start")
#    dispo = getContinuEvent(dispo)
#    occupation = Event.objects.filter(start__contains=date.strftime("%Y-%m-%d")).filter(ressources=ressource).exclude(type="DISPONIBLE").order_by("start")
#    occupation = getContinuEvent(occupation)
#    dispos = getDispo(dispo,occupation)
#    print(dispos)
#    print(dispo)
#    print(occupation)
#    print("same")
#    same = getSimilarDispo(dispos,dispos)
#
#    print(same)
#
#    if not occupation:
#        n = None
#        n = FreeTime(ressource)
#        n.area.clear()
#        for d in dispo:
#            d.start = datetime.combine(date.date(),d.start.time())
#            d.end = datetime.combine(date.date(),d.end.time())
#            n.area.append(Area(d.start,d.end))
#            print("youyou")
#        print('empty')
#        return n
#    n = FreeTime(ressource)
#    for d in dispo:
#        d.start = datetime.combine(date.date(),d.start.time())
#        d.end = datetime.combine(date.date(),d.end.time())
#        n.area.append(Area(d.start,d.end))
#        print(d.start.strftime("%Y-%m-%d %H:%M:%S")+" "+d.end.strftime("%Y-%m-%d %H:%M:%S") + " " + ressource.name)
#        for o in occupation:
#            print(o.start.strftime("%Y-%m-%d %H:%M:%S")+" "+o.end.strftime("%Y-%m-%d %H:%M:%S") + " " + ressource.name)
#            #o.start = o.start.astimezone(timezone.utc).replace(tzinfo=None)
#            #o.end = o.end.astimezone(timezone.utc).replace(tzinfo=None)
#            for a in n.area:
#                print(o.start)
#                print(a.start)
#                # 1
#                if (o.start < a.start and o.end <= a.end) or (o.start > a.end):
#                    print(o.start<a.start)
#                    print(o.end<=a.end)
#                    print(o.start > a.end)
#                    print(o.start.strftime("%Y-%m-%d %H:%M:%S"))
#                    print(a.end.strftime("%Y-%m-%d %H:%M:%S"))
#                    print("1")
#                    pass
#                #2
#                if (o.start < a.start and o.end > a.end):
#                    print("2")
#                    n.area.remove(a)
#                    break
#                #3
#                if (o.start < a.start and (o.end > a.start and o.end <a.end)):
#                    print("3")
#                    a.start = o.end
#                    pass
#                #4
#                if (o.start >= a.start and o.end<a.end):
#                    print("4")
#                    print("normal")
#                    if (o.start is a.start):
#                        a.start=o.end
#                    else:
#                        b = Area(o.end,a.end)
#                        n.area.append(b)
#                        a.end = o.start
#                        #print(a.start.strftime("%Y-%m-%d %H:%M:%S"))
#                        #print(a.end.strftime("%Y-%m-%d %H:%M:%S"))
#                        #print(b.start.strftime("%Y-%m-%d %H:%M:%S"))
#                        #print(b.end.strftime("%Y-%m-%d %H:%M:%S"))
#                    pass
#                #5
#                if (o.start >= a.start and o.end>a.end):
#                    print("5")
#                    a.end = o.start
#                    pass
#    for ev in occupation:
#        print(ev.start.strftime("%Y-%m-%d %H:%M:%S")+" "+ev.end.strftime("%Y-%m-%d %H:%M:%S") + " " + ev.name + " " + ressource.name)
#    return n

class RessourceDispo(object):
    #area = []
    #ressource = Ressource

    def __init__(self):
        self.ressources = []
        self.types = []
        self.dispos = []
        self.prestations = []

    def __str__(self):
        return ('[%s]' % ', '.join(map(str, self.prestations)))

class TypeDispo(object):
    def __init__(self):
        self.name = ''
        self.ressources = []

class Area(object):
    #start = datetime.now()
    #end = datetime.now()

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __str__(self):
        return self.start.strftime("%Y-%m-%d %H:%M:%S")+" "

def getDispo(dispo,occupation):
    sd = []
    for d in dispo:
        #d.start = datetime.combine(date.date(),d.start.time())
        #d.end = datetime.combine(date.date(),d.end.time())
        #n.area.append(Area(d.start,d.end))
        #d.start = d.start.astimezone(timezone.utc).replace(tzinfo=None)
        #d.end = d.end.astimezone(timezone.utc).replace(tzinfo=None)
        sd.append(d)
        print(d.start.strftime("%Y-%m-%d %H:%M:%S")+" "+d.end.strftime("%Y-%m-%d %H:%M:%S") + " " + d.name)
        for o in occupation:
            print(o.start.strftime("%Y-%m-%d %H:%M:%S")+" "+o.end.strftime("%Y-%m-%d %H:%M:%S") + " " + d.name)
            o.start = o.start.astimezone(timezone.utc).replace(tzinfo=None)
            o.end = o.end.astimezone(timezone.utc).replace(tzinfo=None)
            for a in sd:
                print(o.start)
                print(a.start)
                # 1
                if (o.start <= a.start and o.end <= a.end) or (o.start > a.end):
                    print(o.start<a.start)
                    print(o.end<=a.end)
                    print(o.start > a.end)
                    print(o.start.strftime("%Y-%m-%d %H:%M:%S"))
                    print(a.end.strftime("%Y-%m-%d %H:%M:%S"))
                    print("1")
                    pass
                #2
                if (o.start < a.start and o.end > a.end):
                    print("2")
                    sd.remove(a)
                    break
                #3
                if (o.start < a.start and (o.end > a.start and o.end <a.end)):
                    print("3")
                    a.start = o.end
                    pass
                #4
                if (o.start >= a.start and o.end<a.end):
                    print("4")
                    print("normal")
                    if (o.start is a.start):
                        a.start=o.end
                    else:
                        b = Event(start=o.end,end=a.end)
                        sd.append(b)
                        a.end = o.start
                        #print(a.start.strftime("%Y-%m-%d %H:%M:%S"))
                        #print(a.end.strftime("%Y-%m-%d %H:%M:%S"))
                        #print(b.start.strftime("%Y-%m-%d %H:%M:%S"))
                        #print(b.end.strftime("%Y-%m-%d %H:%M:%S"))
                    pass
                #5
                if (o.start >= d.start and o.start < d.end) and (o.end>d.end):
                    print("5")
                    a.end = o.start
                    pass
    return sd

def getSimilarDispo(dispo1,dispo2):
    sd = []
    if(not dispo1 or not dispo2):
        return []

    for d in dispo1:
        #d.start = datetime.combine(date.date(),d.start.time())
        #d.end = datetime.combine(date.date(),d.end.time())
        #n.area.append(Area(d.start,d.end))
        #sd.append(d)
        print(d.start.strftime("%Y-%m-%d %H:%M:%S")+" "+d.end.strftime("%Y-%m-%d %H:%M:%S") + " " + d.name)
        for o in dispo2:
            print(o.start.strftime("%Y-%m-%d %H:%M:%S")+" "+o.end.strftime("%Y-%m-%d %H:%M:%S") + " " + d.name)
            #o.start = o.start.astimezone(timezone.utc).replace(tzinfo=None)
            #o.end = o.end.astimezone(timezone.utc).replace(tzinfo=None)
            # 1
            if (o.start < d.start and o.end <= d.end) or (o.start > d.end):
                print(o.start<d.start)
                print(o.end<=d.end)
                print(o.start > d.end)
                print(o.start.strftime("%Y-%m-%d %H:%M:%S"))
                print(d.end.strftime("%Y-%m-%d %H:%M:%S"))
                print("1")
                pass
            #2
            if (o.start < d.start and o.end > d.end):
                print("2")
                sd.append(d)
                pass
            #3
            if (o.start < d.start and (o.end > d.start and o.end <d.end)):
                print("3")
                b = Event(start=d.start,end=o.end)
                sd.append(b)
                pass
            #4
            if (o.start >= d.start and o.end<=d.end):
                print("4")
                print("normal")
                b = Event(start=o.start,end=o.end)
                sd.append(b)
                pass
            #5
            if (o.start >= d.start and o.start < d.end) and (o.end>d.end):
                print("5")
                b = Event(start=o.start,end=d.end)
                sd.append(b)
                pass
    return sd

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

def getRessourcesDispo(ressources,oldressources,dispos,date):
    for r in ressources:
        if(not r in oldressources):

            dispo = getRessourceDispo(r,date)
            if(not dispo):
                return []

            if(dispos and dispo):
                dispo = getSimilarDispo(dispo,dispos)
            oldressources.append(r)
            ressourc = r.ressources.all()
            res = []
            for rr in ressourc:
                res.append(rr)
            for o in oldressources:
                if(o in res):
                    res.remove(o)

            if(res):
                dispos = getSimilarDispo(getRessourcesDispo(res,oldressources,dispo,date),dispo)
                return dispos
            else:
                return dispo
        pass

def getRessourceDispo(ressource,date):
    day = date.strftime("%a").upper()[0:2]
    dispo = Event.objects.filter(rule=day).filter(ressources=ressource).order_by("start")
    dispo = getContinuEvent(dispo)
    occupation = Event.objects.filter(start__contains=date.strftime("%Y-%m-%d")).filter(ressources=ressource).exclude(type="DISPONIBLE").order_by("start")
    occupation = getContinuEvent(occupation)
    for d in dispo:
            d.start = datetime.combine(date.date(),d.start.time())
            d.end = datetime.combine(date.date(),d.end.time())
    return getDispo(dispo,occupation)

def getTimeInEvent(event):
    delta = event.end - event.start
    print(delta.seconds/60)
    return delta.seconds/60


def prestationDispos(date):
    resdispo = RessourceDispo()
    presta = []
    activ = []
    types = []
    ressources = []
    dispos = []
    q = Prestation.objects.all()
    for pres in q:
        #presta.append(pres)
        qa = pres.activitys.all()
        type = []
        activitys = []
        activ=[]
        for a in qa:
            activitys.append(a)
            qs = a.types.all()
            type = []
            types = []
            for t in qs:
                type.append(t)
                res = t.ressource_set.filter(activitys__in=[a])
                for r in res:
                    d = getRessourcesDispo([r],[],[],date)
                    print(d)
                    for e in d:
                        te = getTimeInEvent(e)
                        if(te>=a.duration):
                            resdispo.dispos.append(e)
                            if(r not in ressources ):
                                ressources.append(r)
                                resdispo.ressources.append(r)
                        print(te)
                        print(r)
                for ress in ressources:
                    if(ress.type not in types):
                        types.append(ress.type)
                        resdispo.types.append(ress.type)
            if(set(types) == set(type)):
                if(a not in activ):
                    activ.append(a)
        if(set(activitys) == set(activ)):
            if(pres not in presta):
                presta.append(pres)
                resdispo.prestations.append(pres)
    return resdispo

def getSelectableRessources(prestation):
    types = []
    typesdispos = []
    for a in prestation.activitys.all():
        for t in a.types.all():
            if(t not in types and t.isSelectable):
                typedispo = TypeDispo()
                typedispo.name = t.name
                typedispo.ressources = t.ressource_set
                typesdispos.append(typedispo)
                types.append(t)

    return typesdispos