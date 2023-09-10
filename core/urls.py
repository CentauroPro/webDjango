from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name="about"),
    path('tutorials/',views.tutorials,name="tutorials"),
    path('login/', views.login_view, name='login'),


]