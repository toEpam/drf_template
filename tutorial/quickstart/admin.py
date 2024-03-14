from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

from .resource import UserResource


class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    resource_class = UserResource


# Unregister the default UserAdmin
admin.site.unregister(User)

# Register UserAdmin with your customizations
admin.site.register(User, UserAdmin)
