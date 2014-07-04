from rest_framework import serializers
from restapi.models import Prestataire,Type,Activite,Prestation,Client,Ressource,Event,Authentication,WEEK_DAY,EVENT_TYPE,Type_Activite
from django.forms import widgets


class AuthenticationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Authentication
        fields = ('url',
                  'api_key')

class PrestataireSerializer(serializers.HyperlinkedModelSerializer):
    use_condition = serializers.CharField(widget=widgets.Textarea)
    class Meta:
        model = Prestataire
        fields = ('url',
                  'authentication', 'name', 'timezone', 'use_condition')


class TypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Type
        fields = ('url','id',
                'name', 'isSelectable', 'isReservable','prestataire')

class Type_ActiviteSerializer(serializers.ModelSerializer):
    #type = serializers.Field(source='type.name')
    #activite = serializers.Field(source='activite.name')

    class Meta:
        model = Type_Activite
        #fields = ('number', 'type', 'activite',)

class ActiviteSerializer(serializers.ModelSerializer):
    #types = Type_ActiviteSerializer(source='types',many=True)
    #types = Type_ActiviteSerializer(source='type_activite_set',many=True)
    #types = serializers.Serializer(widget=widgets.SelectMultiple,data=Type.objects.all(),instance=Type)
    class Meta:
        model = Activite
    #    fields = (#'url',
    #            'name', 'duration', 'types','prestataire')

class PrestationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prestation
        #fields = ('url',
        #        'name', 'duration','price', 'activitys','activityOrder','prestataire')

class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ('url',
                'name', 'mail','adress', 'phone','prestataire')

class RessourceSerializer(serializers.HyperlinkedModelSerializer):

    ressources = serializers.HyperlinkedRelatedField(view_name='ressource-detail', many=True)
    class Meta:
        model = Ressource
        fields = ('url','id',
                'name','email','isAdmin','type','activitys','ressources','prestataire')

class EventSerializer(serializers.ModelSerializer):
    ressources = serializers.HyperlinkedRelatedField(view_name='ressource-detail', many=True)
    class Meta:
        model = Event
        fields = (
                'name','type','state','start','end','rule','client','prestation','activity','ressources','prestataire')

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        widget=widgets.PasswordInput(),
        required=False
    )


class HoraireSerializer(serializers.ModelSerializer):
    rule = serializers.ChoiceField(choices=WEEK_DAY)
    ressources = serializers.HyperlinkedRelatedField(view_name='ressource-detail', many=True)
    class Meta:
        model = Event
        fields = ('rule',
                  'start', 'end','ressources','prestataire','state')

class CongeSerializer(serializers.ModelSerializer):
    ressources = serializers.HyperlinkedRelatedField(view_name='ressource-detail', many=True)
    class Meta:
        model = Event
        fields = (
                  'start', 'end','ressources','prestataire','state')

class AreaSerializer(serializers.Serializer):
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def restore_object(self, attrs, instance=None):
       """
       Given a dictionary of deserialized field values, either update
       an existing model instance, or create a new model instance.
       """
       if instance is not None:
           instance.start = attrs.get('start',instance.start)
           instance.end = attrs.get('end',instance.end)
           return instance
       return AreaSerializer(**attrs)


class FreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
                'start','end')

class DispoSerializer(serializers.Serializer):
    ressources = RessourceSerializer(many=True)
    prestations = PrestationSerializer(many=True)
    types = TypeSerializer(many=True)
    dispos = FreeSerializer(many=True)

    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.ressources = attrs.get('ressource',instance.ressources)
            instance.prestations = attrs.get('area',instance.prestations)
            instance.types = attrs.get('area',instance.types)
            instance.dispos = attrs.get('area',instance.dispos)
            return instance
        return DispoSerializer(**attrs)

class SelectableRessourceSerializer(serializers.Serializer):
    name = serializers.CharField()
    ressources = RessourceSerializer(many=True)


    def restore_object(self, attrs, instance=None):

        if instance is not None:
            instance.name = attrs.get('name',instance.name)
            instance.ressources = attrs.get('ressources',instance.ressources)
            return instance
        return SelectableRessourceSerializer(**attrs)