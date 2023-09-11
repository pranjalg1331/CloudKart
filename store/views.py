from django.shortcuts import render,redirect
from django.http import HttpResponse
from register.models import Profile
from .models import Product,Category,Cart,CartItem
# Create your views here.
def store(request):
    if request.method=='GET':
        products=Product.objects.all()
        categories=Category.objects.all()
        categroy_id=request.GET.get('category')
        if categroy_id:
            products=Product.products_bycategory(categroy_id)
        data={}
        
        user_email=request.session.get('user_email')
        # print(user_email)
        if user_email:
            profile=Profile.objects.get(email=user_email)
            cart=Cart.objects.get(user=profile)
            cartitems=CartItem.objects.filter(cart=cart)
            product_incartitem=[]
            for a in cartitems:
                product_incartitem.append(a.product)
            print(product_incartitem)   
            data['cartitems']=cartitems
            data['profile']=profile
            data['product_incartitem']=product_incartitem
            
            
        data['products']=products
        data['categories']=categories
        
        return render(request,'store.html',data)
    else:
        user_email=request.session.get('user_email')
        if user_email:
            profile=Profile.objects.get(email=user_email)
            cart=Cart.objects.get(user=profile)
            cartitems=CartItem.objects.filter(cart=cart)
            
            product_id=request.POST.get('product_id')
            if product_id:
                product=Product.objects.get(id=product_id)
                # print(product)
                cartitem=CartItem(cart=cart,product=product)
                cartitem.save()
            
        return redirect('storepage')
    
    

    