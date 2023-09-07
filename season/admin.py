from django.contrib import admin

# Register your models here.
from .models import Season

# Register your models here.
class SeasonAdmin(admin.ModelAdmin):

    readonly_fields=('created','updated')

admin.site.register(Season, SeasonAdmin)