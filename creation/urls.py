from django.urls import path
from . import views

urlpatterns = [
    path('',views.creation,name="creation"),
]