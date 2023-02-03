from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return render(request, 'index.html')
    #return HttpResponse('<h1> Hey, Welcome</h1')
def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})