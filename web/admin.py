from django.contrib import admin
from web.models import *
# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'blacklisted_by')
admin.site.register(Place, PlaceAdmin)


class BlackListAdmin(admin.TabularInline):
    model = BlackList

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'blacklist', 'active')
    inlines = [BlackListAdmin]
admin.site.register(Person, PersonAdmin)


class QuorumAdmin(admin.ModelAdmin):
    list_display = ('person', 'uuid', 'lunch')
admin.site.register(Quorum, QuorumAdmin)
