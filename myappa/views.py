from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

    
# Create your views here.
def index(request): 
    
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})
    #return HttpResponse('<h1> Hey, Welcome</h1')
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if username=='':
              messages.info(request, 'UserName is empty')
              return redirect('register')
        elif email=='':
              messages.info(request, 'E-mail is empty')
              return redirect('register')
        elif password=='':
              messages.info(request, 'Password is empty')
              return redirect('register')
            
        elif password==password2:
             if User.objects.filter(email=email).exists():
                 messages.info(request, 'Email already Used')
                 return redirect('register')
             elif User.objects.filter(username=username).exists():
                 messages.info(request, 'Username already Used')
                 return redirect('register')
             else:
                 user = User.objects.create_user(username=username, email=email, password=password)
                 user.save()
                 return redirect('login')
        else:
            messages.info(request, 'Password Not The same')
            return redirect('register')     
    else:
        return render(request,'register.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})