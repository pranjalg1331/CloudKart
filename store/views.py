from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category
# Create your views here.
def store(request):
    if request.method=='GET':
        products=Product.objects.all()
        categories=Category.objects.all()
        categroy_id=request.GET.get('category')
        if categroy_id:
            products=Product.products_bycategory(categroy_id)
        data={}
        data['products']=products
        data['categories']=categories
        return render(request,'store.html',data)
    else:
        
        return HttpResponse("hello")