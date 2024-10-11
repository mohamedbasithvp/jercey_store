from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    featured_product = Products.objects.order_by('priority')[:4]
    latest_product = Products.objects.order_by('-id')[:4]
    context = {
        'featured_products': featured_product,
        'latest_products': latest_product
    }
    return render(request, 'index.html', context)


def list_products(request):
    """_summary_
    returns product list page
    Args:
        request (_type_): _description_
        
    Returns:
        _type_: _description_
    """
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    product_list = Products.objects.order_by('priority')
    product_paginator = Paginator(product_list, 4)
    product_list = product_paginator.page(page)
    context = {'products': product_list}
    return render(request, 'products_list.html', context)


# single product nte view ne vendi
def detail_products(request, pk):
    product = Products.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)