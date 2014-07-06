import time

from dateutil.parser import parse
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from restapi.functions import getSelectableRessources

from restapi.models import Prestataire,Type,Activite,Prestation,Client,Ressource,Event,Authentication
from restapi.serializers import PrestataireSerializer,TypeSerializer,ActiviteSerializer,PrestationSerializer\
    ,ClientSerializer,EventSerializer,RessourceSerializer,AuthenticationSerializer,HoraireSerializer\
    ,CongeSerializer, DisponibiliteSerializer
from restapi.permissions import UnsafeSessionAuthentication


class AuthenticationViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Authentication.
    """
    queryset = Authentication.objects.all()
    serializer_class = AuthenticationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PrestataireViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Prestataire.
    """
    queryset = Prestataire.objects.all()
    serializer_class = PrestataireSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TypeViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Type.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ActiviteViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Activity.
    """
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PrestationViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Prestation.
    """
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ClientViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Client.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RessourceViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Ressource.
    """
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer
    permission_classes = (permissions.AllowAny,)

class EventViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HoraireViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Horaire.
    """
    queryset = Event.objects.filter(type='DISPONIBLE').order_by('start')
    serializer_class = HoraireSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.type = 'DISPONIBLE'
        obj.state = 'CONFIRMED'

    # def the ressource after save the event (maybe use in next version)
    #def post_save(self, obj, created=False):
    #    if(obj.ressources.count() == 0):
    #        obj.ressources.clear()
    #        obj.ressources.add(Ressource.objects.get(user=User.objects.get(username=self.request.user).id))
    #        obj.save()

class CongeViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents Conge.
    """
    queryset = Event.objects.filter(type='CONGE').order_by('start')
    serializer_class = CongeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.type = 'CONGE'
        obj.state = 'CONFIRMED'

    # def the ressource after save the event (maybe use in next version)
    #def post_save(self, obj, created=False):
    #    if(obj.ressources.count() == 0):
    #        obj.ressources.clear()
    #        obj.ressources.add(Ressource.objects.get(user=User.objects.get(username=self.request.user).id))
    #        obj.save()


class DispoViewSet(viewsets.ViewSet):
    """
    This endpoint presents Dispo, date is necessary.
    """

    def list(self, request):
        session = time.time()
        queryset=getSelectableRessources(parse(request.QUERY_PARAMS.get('date')),Prestation.objects.filter(
            id=int(request.QUERY_PARAMS.get('prestation'))).first(),session)
        serializer = DisponibiliteSerializer(queryset)

        return Response(serializer.data)


class ReservationViewSet(viewsets.ViewSet):
    """
    This endpoint is for book a prestation.
    """
    authentication_classes = (UnsafeSessionAuthentication,)

    def create(self,request):
        accept = (request.DATA['accept'] == "true")
        sessionid = request.DATA['sessionid']
        num_api = request.DATA['api_key']
        name=request.DATA['name']
        email=request.DATA['email']
        adress=request.DATA['adress']
        tel=request.DATA['tel']
        if(not accept):
            return Response("Erreur: Veuillez accepter les conditions")
        auth = Authentication.objects.filter(api_key=num_api).first()
        prestataire = Prestataire.objects.filter(authentication=auth).first()
        client = Client(name=name,mail=email,adress=adress,phone=tel,prestataire=prestataire)
        client.save()
        a = Event.objects.filter(session=sessionid).all()
        prestation = None
        start = None
        end = None
        for e in a:
            if(not prestation):
                prestation = e.prestation
            if(not start):
                start = e.start
                end = e.end
            if(e.start < start):
                start = e.start
            if(e.end > end):
                end = e.end
            e.session = None
            e.client = client
            e.save()
        event = Event(start=start,end=end,client=client,prestation=prestation,type="OCCUPE",state="WAITING",prestataire=prestataire)
        event.save()
        return Response({"success":"true"})




















