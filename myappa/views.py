from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def createFeatures():
    
    
    features = []
    
    return features
    
# Create your views here.
def index(request): 
    
    features = createFeatures()
    return render(request, 'index.html', {'features': features})
    #return HttpResponse('<h1> Hey, Welcome</h1')
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})