from django.contrib import admin
admin.autodiscover()

from snippets import views
from restapi import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'snippets', views.SnippetViewSet)
#router.register(r'users', views.UserViewSet)
router.register(r'prestataire', views.PrestataireViewSet)
router.register(r'type', views.TypeViewSet)
router.register(r'activite', views.ActiviteViewSet)
router.register(r'prestation', views.PrestationViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'ressource', views.RessourceViewSet)
router.register(r'authentication', views.AuthenticationViewSet)
router.register(r'horaire', views.HoraireViewSet)
router.register(r'conge', views.CongeViewSet)
router.register(r'dispo', views.DispoViewSet)
router.register(r'type_activite', views.Type_ActiviteViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartbooking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)


