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
        'segment'  : 'constructors',
        'parent'   : 'f1Wiki',
        'products': products
    }
    return render(request, 'f1Wiki/constructors.html')

def show_example_wikipedia_page(request):
    # 위키피디아 예시 URL
    example_url = "https://w.wiki/CGiX"
    return render(request, 'f1Wiki/constructors.html', {'example_url': example_url})