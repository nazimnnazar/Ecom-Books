from django.shortcuts import render
from .models import*
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def frontpage(request):
    return render(request,'frontpage.html',)

def book(request,c_slug=None):
    c_slug=None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(Categ, slug=c_slug)
        prodt = Product.objects.filter(category=c_page, available=True)
    else:
        prodt = Product.objects.all().filter(available=True)
    cat = Categ.objects.all()   

    product=Product.objects.all()
    pag = Paginator(Product.objects.all(),8)
    page = request.GET.get('page')
    venues = pag.get_page(page)
    context={
        'product':product,
        'product':venues,
        'pr':prodt,
        'ct':cat,
        
        }
    return render(request,'product.html',context)

def product_views(request,c_slug,product_slug):
    try:
        prod=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'shop.html',{"product":prod})
