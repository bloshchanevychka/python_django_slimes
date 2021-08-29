from django.contrib import admin
from .models import Action, Slime, SlimeTypes
# Register your models here.


class SlimeAdmin(admin.ModelAdmin):
    fields = ['name','color', 'action','type']

admin.site.register(Slime, SlimeAdmin)


admin.site.register(Action)
#admin.site.register(Slime)
admin.site.register(SlimeTypes)
