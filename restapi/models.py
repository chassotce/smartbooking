import time
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
import pytz


# List of timezones
TIMEZONES = [(x, x) for x in pytz.common_timezones]

# Event type list
EVENT_TYPE = (
    ('OCCUPE','OCCUPE'),
    ('CONGE','CONGE'),
    ('PROVISOIRE','PROVISOIRE'),
    ('DISPONIBLE','DISPONIBLE'),
)

# Event state list
EVENT_STATE = (
    ('WAITING','WAITING'),
    ('CONFIRMED','CONFIRMED'),
    ('CANCELED','CANCELED'),
)

# Day of week list
WEEK_DAY = (
    ('MO','LUNDI'),
    ('TU','MARDI'),
    ('WE','MERCREDI'),
    ('TH','JEUDI'),
    ('FR','VENDREDI'),
    ('SA','SAMEDI'),
    ('SU','DIMANCHE')
)

'''
MODELS
'''
# Prestataire model
class Prestataire(models.Model):
    name = models.CharField(max_length=255)
    timezone = models.CharField(choices=TIMEZONES,default='Europe/Zurich',max_length=250)
    use_condition = models.CharField(max_length=1024)
    authentication = models.ForeignKey('Authentication')

    def __str__(self):
        return self.name

# Authentication model
class Authentication(models.Model):
    api_key = models.CharField(unique=True,max_length=255)

# Type model
class Type(models.Model):
    name = models.CharField(max_length=255)
    isSelectable = models.BooleanField()
    number = models.PositiveIntegerField()
    ressources = models.ManyToManyField('Ressource')
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):
        return self.name

# Activite model
class Activite(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    types = models.ManyToManyField(Type)
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):
        return self.name

# Prestation model
class Prestation(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    activitys = models.ManyToManyField('Activite')
    activityOrder = models.CharField(max_length=1024)
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):
        return self.name

# Client model
class Client(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):
        return self.name

# Ressource model
class Ressource(models.Model):
    user = models.OneToOneField(User,blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    isAdmin = models.BooleanField()
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):
        return self.name

# Manager to add function to Event model
class EventManager(models.Manager):

    # Delete all event with session > 5 min
    def deleteOld(self):
        es = self.exclude(session__isnull=True).all()
        ts = time.time()
        st = datetime.fromtimestamp(ts)
        st = st - timedelta(minutes=5)
        for e in es:
            if(datetime.fromtimestamp(e.session) < st):
                e.delete()

# Event model
class Event(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255,choices=EVENT_TYPE)
    state = models.CharField(max_length=255,choices=EVENT_STATE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    rule = models.CharField(max_length=255,blank=True,null=True)
    client = models.ForeignKey('Client',blank=True,null=True)
    prestation = models.ForeignKey('Prestation',blank=True,null=True)
    activity = models.ForeignKey('Activite',blank=True,null=True)
    ressource = models.ForeignKey('Ressource',blank=True,null=True)
    session = models.FloatField(blank=True,null=True)
    prestataire = models.ForeignKey('Prestataire')
    objects=EventManager()

    def __str__(self):
        return self.name+" "+self.type


'''
OBJECTS
'''
# Object content name of type and ressources
class TypeDispo(object):
    def __init__(self):
        self.name = ''
        self.ressources = []

# Object content event disponible and typeDispo
class Disponibilite(object):
    def __init__(self):
        self.typeDispo = []
        self.event = None

# Object contenent reservable event
class Reservable(object):
    def __init__(self):
        self.event = None
