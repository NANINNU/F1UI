from django.shortcuts import render,get_object_or_404
from apps.common.models import Product
from django.core import serializers
import requests


def index(request):
    products = serializers.serialize('json', Product.objects.all())
    context = {
        'segment'  : 'charts',
        'parent'   : 'apps',
        'products': products
    }
    return render(request, 'apps/charts.html', context)

def show_example_wikipedia_page(request):
    # 위키피디아 예시 URL
    example_url = "https://w.wiki/CGiX"
    return render(request, 'charts.html', {'example_url': example_url})

