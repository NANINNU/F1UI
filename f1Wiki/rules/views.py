from django.shortcuts import render
from apps.common.models import Product
from django.core import serializers

#import for namuwiki
from django.http import FileResponse
import os


# Create your views here.

def index(request):
    products = serializers.serialize('json', Product.objects.all())
    context = {
        'segment'  : 'rules',
        'parent'   : 'f1Wiki',
        'products': products
    }
    return render(request, 'f1Wiki/rules.html', context)


def serve_pdf(request):
    pdf_path = os.path.join('static/dist/img/f1Ruls.pdf', 'f1Ruls.pdf')  # 실제 PDF 파일 경로
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
