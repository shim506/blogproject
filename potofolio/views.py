from django.shortcuts import render
from .models import Portofolio

def potofolio(request):
    potofolio = Portofolio.objects
    return render(request , 'potofolio.html',{'potofolios':potofolio})
    
# Create your views here.
