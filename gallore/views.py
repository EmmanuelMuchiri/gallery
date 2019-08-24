import datetime as dt
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image
# Create your views here.
def welcome(request):
    return render(request,'index.html')

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"pics/pics.html", {"image":image})
