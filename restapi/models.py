from django.db import models
from django.contrib.auth.models import User
import pytz

# Create your models here.
TIMEZONES = [(x, x) for x in pytz.common_timezones]
EVENT_TYPE = (
    ('OCCUPE','OCCUPE'),
    ('CONGE','CONGE'),
    ('PROVISOIRE','PROVISOIRE'),
    ('DISPONIBLE','DISPONIBLE'),
)

EVENT_STATE = (
    ('WAITING','WAITING'),
    ('CONFIRMED','CONFIRMED'),
    ('CANCELED','CANCELED'),
)

WEEK_DAY = (
    ('MO','LUNDI'),
    ('TU','MARDI'),
    ('WE','MERCREDI'),
    ('TH','JEUDI'),
    ('FR','VENDREDI'),
    ('SA','SAMEDI'),
    ('SU','DIMANCHE')
)


class Prestataire(models.Model):
    name = models.CharField(max_length=255)
    timezone = models.CharField(choices=TIMEZONES,default='Europe/Zurich',max_length=250)
    use_condition = models.CharField(max_length=1024)
    authentication = models.ForeignKey('Authentication')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Authentication(models.Model):
    api_key = models.CharField(unique=True,max_length=255)


class Type(models.Model):
    name = models.CharField(max_length=255)
    isSelectable = models.BooleanField()
    number = models.PositiveIntegerField()
    ressources = models.ManyToManyField('Ressource')
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Activite(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    types = models.ManyToManyField(Type)
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Prestation(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    activitys = models.ManyToManyField('Activite')
    activityOrder = models.CharField(max_length=1024)
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Ressource(models.Model):
    user = models.OneToOneField(User,blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    isAdmin = models.BooleanField()
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

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
    ressources = models.ManyToManyField('Ressource',blank=True,null=True)
    session = models.PositiveIntegerField()
    prestataire = models.ForeignKey('Prestataire')

    def __str__(self):              # __unicode__ on Python 2
        return self.name+" "+self.type