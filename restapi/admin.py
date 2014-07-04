from django.contrib import admin
from restapi.models import Ressource
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class RessourceInline(admin.StackedInline):
    model = Ressource
    can_delete = False
    verbose_name_plural = 'ressource'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (RessourceInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)