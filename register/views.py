from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
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
            user.save()
            login(request, user)
            return redirect('storepage')
        else:
            return render(request, 'signup.html', {'form': form})
        


    
    
    