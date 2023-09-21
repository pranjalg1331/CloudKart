from django.shortcuts import render,redirect
from django.http import HttpResponse
from register.models import Profile
from .models import Product,Category,Cart,CartItem
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse,HttpResponseBadRequest

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
        
        print(user_email)
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
    
    

def cart(request):
    if request.method=='GET':
        user_email=request.session.get('user_email')
        # print(user_email)
        if(user_email):
            user=Profile.objects.get(email=user_email)
            print(user)
            cart=Cart.objects.get(user=user)
            cartitems=CartItem.objects.filter(cart=cart)
            data={}
            data['cartitems']=cartitems
            return render(request,'cart.html',data)
        
        return redirect('signup')
    
def updateQuantity(request,itemId):
    if request.method=="POST":
        cartitem=CartItem.objects.get(id=itemId)
        if(cartitem):
            print(cartitem)
            item_quant=int(request.POST.get('quantity'))
            print(item_quant)
            cartitem.quantity=item_quant
            cartitem.save()
            return JsonResponse({'status':'quantity changed'})
        
        # else:
        #     data={"msg":"did not work"}
        #     return JsonResponse(data)
    return redirect('/')
    # if is_ajax:
    #     if request.method=='POST':
    #         cartitem=CartItem.objects.get(id=itemId)
    #         data=json.loads(request.body.decode('utf-8'))
    #         quantity=data.get('quantity')
    #         if quantity is not None:
    #             print(quantity)
    #             cartitem.quantity=quantity
    #             return JsonResponse({'status': 'quantity changed!'})
    #     print("hello")
    #     return JsonResponse({'status': 'Invalid request'}, status=400)
    # else:
    #     return HttpResponseBadRequest('Invalid request')
        
    