from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
        }
    return render(request,'index.html',context)
    #return HttpResponse("Homepagu")
def about(request):
    # return HttpResponse("This is about page")
     return render(request,'about.html')
def services(request):
    # return HttpResponse("Services here")
     return render(request,'services.html')
def contact(request):
    # return HttpResponse("Services here")
    if request.method == "POST":
        name  =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact= Contact(name = name,email=email,phone =phone,desc=desc)
        contact.save()
        messages.success(request, 'Your response has been noted!')
         
    return render(request,'contacts.html')
def home(request):
    # return HttpResponse("Services here")
     return render(request,'home.html')
 
def joshi(request):
    # return HttpResponse("Services here")
     return render(request,'index.html')

