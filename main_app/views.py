from unicodedata import name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Add the Cat class & list and view function below the imports
class Cat: 
    def __init__(self, name, breed, description,age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        
cats = [
    Cat('Lolo', 'tabby', 'smelly', 2),
    Cat('Moomoo','calico', 'angy', 3),
    Cat('Chester','black','mysterious', 30)
]

#Define the home view
def home(request):
    return HttpResponse('<h1>HELLLOOOO</h1>')


def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})

