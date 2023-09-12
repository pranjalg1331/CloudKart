from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
import uuid
from .models import Profile
from store.models import Cart
from . import utils
# # Create your views here.
def signup(request):
   
    if request.method=='GET':
        form = CreateUserForm()
        
        context={
            'form':form
        }
        return render(request,'signup.html',context)
    else :
        form = CreateUserForm(request.POST)
       
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.token=str(uuid.uuid4())
            utils.send_email_token(user.email,user.token)
            user.save()
            cart=Cart(user=user)
            cart.save()
            print(user.email)
            
            # user_email=request.session.get('user_email')
            # print(user_email)
            login(request, user)
            request.session['user_email']=user.email
            return redirect('storepage')
        else:
            return render(request, 'signup.html', {'form': form})
        


    
def verify(request,token):
    user=Profile.objects.get(token=token)
    print(user)
    if user:
        user.is_authenticated=True
        user.save()
        return redirect('storepage')
    else:
        return HttpResponse("Invalid token")
    