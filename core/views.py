from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,"core/about.html")
def tutorials(request):
    return render(request,"core/tutorials.html")
