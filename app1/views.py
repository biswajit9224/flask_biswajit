from django.shortcuts import render

# Create your views here.
from app1.models import *

def topic(request):
    topics=Topic.objects.all()
    return render(request,'topic.html',context={'topics':topics})

def webpage(request):
    #webpages=Webpage.objects.all()
    webpages=Webpage.objects.order_by('name')
    return render(request,'webpage.html',context={'webpages':webpages})

def access_records(request):
    access_record=Access_Records.objects.all()
    return render(request,'access_records.html',context={'access_record':access_record})
    