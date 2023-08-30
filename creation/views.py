from django.shortcuts import render
from .models import Project
# Create your views here.
def creation(request):
    
    projects=Project.objects.all()
    return render(request,"creation/creation.html",{'manualidades': projects})# consultado la liata para poder visualizar en web 
