from django.shortcuts import render
from django.http import *
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
def index(request):
    return render(request, 'searches.html')

def about_us(request):
    return render(request, 'about_us.html')

def search(request):
    if request.method=='GET':
        srch = request.GET['query']

        if srch:
            match =ProductInfo.objects.filter( Q(product_name__icontains=srch) )
            if match :
               
                return render(request,'search.html',{'sr': match})
            else :
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')
