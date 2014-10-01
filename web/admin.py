from django.contrib import admin
from web.models import *
# Register your models here.


admin.site.register(Place)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail')
admin.site.register(Person, PersonAdmin)


class QuorumAdmin(admin.ModelAdmin):
    list_display = ('person', 'uuid', 'lunch')
admin.site.register(Quorum, QuorumAdmin)
