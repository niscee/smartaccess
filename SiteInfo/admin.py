from django.contrib import admin
from .models import SiteInfo

# Register your models here.

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
     def has_add_permission(self, request, obj=None):
        return False