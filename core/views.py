from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login

# Create your views here.

def about(request):
    return render(request,"core/about.html")
def tutorials(request):
    return render(request,"core/tutorials.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Aquí se pasa el objeto 'user' como segundo argumento
            return redirect('admin:index')  # Redirigir al panel de administración
        else:
            # El inicio de sesión falló, puedes manejarlo aquí
            pass

    return render(request, 'core/login.html')
