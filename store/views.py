from django.shortcuts import render,redirect
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from register.models import Profile
from .models import Product,Category,Cart,CartItem
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse,HttpResponseBadRequest

# Create your views here.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


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
            total_price=Cart.getTotalPrice(cart)
            
            cartitems=CartItem.objects.filter(cart=cart)
            data={}
            data['user']=user
            data['cartitems']=cartitems
            data['total_price']=total_price
            razorpay_order = razorpay_client.order.create(dict(amount=total_price*100,
                                                       currency='INR',
                                                       payment_capture='0'))
            razorpay_order_id = razorpay_order['id']
            
            callback_url='paymenthandler/'
            data['razorpay_order_id'] = razorpay_order_id
            data['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
            data['razorpay_amount'] = total_price*100
            data['currency'] = 'INR'
            data['callback_url'] = callback_url
            
            return render(request,'cart.html',data)
        
        return redirect('signup')
    else:
        user_email=request.session.get('user_email')
        # print(user_email)
        if(user_email):
            user=Profile.objects.get(email=user_email)
            cart=Cart.objects.get(user=user)
            total_price=Cart.getTotalPrice(cart)
            cartitems=CartItem.objects.filter(cart=cart)
            data={}
            data['user']=user
            data['cartitems']=cartitems
            data['total_price']=total_price
        return render(request,'checkout.html',data)
    
def updateQuantity(request,itemId):
    if request.method=="POST":
        cartitem=CartItem.objects.get(id=itemId)
        
        if(cartitem):
            print(cartitem)
            item_quant=int(request.POST.get('quantity'))
            
            print(item_quant)
            cartitem.quantity=item_quant
            cartitem.save()
            
            cart=cartitem.cart
            total_price=Cart.getTotalPrice(cart)
            cart.save()
            
            data=request.POST
            print(data)
            
            return JsonResponse({'data':total_price,'status':'quantity changed'})

    return redirect('/')

@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = request.POST.get('razorpay_amount')  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'login.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'cart.html')
            else:
 
                # if signature verification fails.
                return render(request, 'cart.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
    
def checkout(request):
    return render(request,'checkout.html')
