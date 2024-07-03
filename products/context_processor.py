from.models import product_category, Product,Order,OrderItem,Type
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.shortcuts import redirect,render
from django.http import JsonResponse
import json
from django.db.models import Q



def product_list(request):
    q= request.GET.get('q')
    if request.GET.get('q') if request.GET.get('q') != None else "":
        all_products  = Product.objects.filter(Q(product_category__name__icontains=q)|
                                               Q(name__icontains=q)|
                                               Q(product_detail__icontains=q)
                                               
                                               )
    else:
        all_products = Product.objects.all()
    all_categories  =  product_category.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(all_products, 20)
    try:
        all_products  = paginator.page(page)        
    except PageNotAnInteger:
        all_products  = paginator.page(1)
    except EmptyPage:
        all_products  = paginator.page(paginator.num_pages)
    context  = {
        "pdts":all_products,
        "cats":all_categories,
        
    }
    return context   
