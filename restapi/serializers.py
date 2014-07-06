from rest_framework import serializers
from django.forms import widgets

from restapi.models import Prestataire,Type,Activite,Prestation,Client,Ressource,Event,Authentication,WEEK_DAY

# Authentication serializer
class AuthenticationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= Authentication
        fields = ('url','id',
                  'api_key')

# Prestataire serializer
class PrestataireSerializer(serializers.HyperlinkedModelSerializer):
    use_condition = serializers.CharField(widget=widgets.Textarea)
    class Meta:
        model = Prestataire
        fields = ('url','id',
                  'authentication', 'name', 'timezone', 'use_condition')

# Type serializer
class TypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Type
        fields = ('url','id',
                'name','number','isSelectable','ressources','prestataire')

# Activite serializer
class ActiviteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activite
        fields = ('url','id',
                'name', 'duration', 'types','prestataire')

# Prestation serializer
class PrestationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Prestation
        fields = ('url','id',
                'name', 'duration','price', 'activitys','activityOrder','prestataire')

# Client serializer
class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ('url','id',
                'name', 'mail','adress', 'phone','prestataire')

# Ressource serializer
class RessourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ressource
        fields = ('url','id',
                'name','email','isAdmin','prestataire')

# Event serializer
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url',
                'name','type','state','start','end','rule','client','prestation','activity','ressource','session','prestataire')

# Horaire serializer
class HoraireSerializer(serializers.HyperlinkedModelSerializer):
    rule = serializers.ChoiceField(choices=WEEK_DAY)
    class Meta:
        model = Event
        fields = ('url','rule',
                  'start', 'end','ressource','prestataire')

class CongeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url',
                  'name','start', 'end','ressource','prestataire')


# SelectableRessources serializer
class SelectableRessourceSerializer(serializers.Serializer):
    name = serializers.CharField()
    ressources = RessourceSerializer(many=True)


    def restore_object(self, attrs, instance=None):

        if instance is not None:
            instance.name = attrs.get('name',instance.name)
            instance.ressources = attrs.get('ressources',instance.ressources)
            return instance
        return SelectableRessourceSerializer(**attrs)

# Disponibilite serializer
class DisponibiliteSerializer(serializers.Serializer):
    event = EventSerializer()
    typeDispo = SelectableRessourceSerializer(many=True)


    def restore_object(self, attrs, instance=None):

        if instance is not None:
            instance.typeDispo = attrs.get('typeDispo',instance.typeDispo)
            instance.event = attrs.get('event',instance.event)
            return instance
        return SelectableRessourceSerializer(**attrs)