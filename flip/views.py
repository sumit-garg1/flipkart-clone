from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from flip.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request,'flip.html')
def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
    # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
    # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')
# def logout(request):
#     return render(request,'index.html')
def Contact(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        country=request.POST.get("country")
        subject=request.POST.get("subject")
        new_contact = contact(firstname=firstname, lastname=lastname, country=country, subject=subject)
        new_contact.save()
        messages.success(request, "your message will be delivered.")  
    return render(request, 'contact.html') 
def cart(request):
    return render(request,'cart.html')