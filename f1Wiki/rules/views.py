from django.shortcuts import render
from apps.common.models import Product
from django.core import serializers

#import for namuwiki
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render



# Create your views here.

def index(request):
    products = serializers.serialize('json', Product.objects.all())
    context = {
        'segment'  : 'rules',
        'parent'   : 'f1Wiki',
        'products': products
    }
    return render(request, 'f1Wiki/rules.html')