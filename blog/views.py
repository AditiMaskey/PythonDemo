from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# functional based
def index(request):
# key-value
    data = {
        'title':'Index pageeee',
        'name':'Ads',  
        'users':['A','Ad'],
    }
    return render(request, 'index.html',data)

def about(request):
   about = {
    'title':'hello About',
   } 
   return render(request, 'about.html',about )
   

def contact(request):
    contact = {
        "name":'HELLO',
        "title":"Contact Page",
         }
    return render(request, 'contact.html', contact)

def response(request):
    return HttpResponse("This is a http response")