from django.shortcuts import render
from apps.f1.models import Drivers, Constructors

def f1_search(request):
    query = request.GET.get('query', '')  # 검색어
    category = request.GET.get('category', 'drivers')  # 기본 카테고리는 'drivers'
    results = []

    # 카테고리에 따라 검색 수행
    if category == 'drivers':
        results = Drivers.objects.filter(name__icontains=query)  # Drivers 검색
    elif category == 'constructors':
        results = Constructors.objects.filter(name__icontains=query)  # Constructors 검색

    context = {
        'results': results,
        'query': query,
        'query_category': category,
    }
    return render(request, 'apps/F1_Search.html', context)
