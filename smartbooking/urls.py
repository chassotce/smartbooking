from django.contrib import admin
admin.autodiscover()


from restapi import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'prestataire', views.PrestataireViewSet)
router.register(r'type', views.TypeViewSet)
router.register(r'activite', views.ActiviteViewSet)
router.register(r'prestation', views.PrestationViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'ressource', views.RessourceViewSet)
router.register(r'authentication', views.AuthenticationViewSet)
router.register(r'horaire', views.HoraireViewSet,base_name='horaire')
router.register(r'conge', views.CongeViewSet,base_name='conge')
router.register(r'dispo', views.DispoViewSet,base_name='dispo')
router.register(r'reservation', views.ReservationViewSet,base_name='reservation')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)


