from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def createFeatures():
    feature1 = Feature()
    feature1.id = 0
    feature1.name='Fast 0'
    feature1.details='0 - Our service is very quick'
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name='Fast 1'
    feature2.details='1 - Our service is very quick'
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name='Fast 2'
    feature3.details='2 - Our service is very quick'
    
    feature4 = Feature()
    feature4.id = 2
    feature4.name='Fast 2'
    feature4.details='3 - Our service is very quick'
    
    features = [feature1,feature2,feature3,feature4]
    
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