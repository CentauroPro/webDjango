from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    readonly_fields=('created','updated')
    list_display = ('id', 'image', 'created', 'updated')
    search_fields = ('image', 'created')
admin.site.register(Project,ProjectAdmin)

