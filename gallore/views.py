import datetime as dt
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Location,categories
# Create your views here.
def welcome(request):
    return render(request,'index.html')

def image(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()
   
    if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)

    elif 'category' in request.GET and request.GET['category']:
        cat = request.GET.get('category')
        images = Image.view_category(cat)
        return render(request, 'pics/pics.html', {"name":name,"images":images,"cat":cat })
    

    return render(request, 'pics/pics.html', {"images":images,"location":location,"category":category})
