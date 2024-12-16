from http.client import HTTPResponse
from django.shortcuts import redirect, render
from ShopApp.form import UserReg 
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    prods=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"Trending":prods})

def register(request):
    form=UserReg()
    if request.method=='POST':
        form=UserReg(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successful")
            return redirect('userlogin')
        
    return render(request,"shop/register.html",{"register":form})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successful")
                return redirect("collections")
            else:
                messages.warning(request,"Login failed")
                return redirect("userlogin")
        return render(request,'shop/login.html')

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successful")
        return redirect("userlogin")
    
def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"Category":category})

def Viewcollections(request,cname):
    if(Category.objects.filter(name=cname,status=0)):
        prods=Product.objects.filter(category__name=cname)
        return render(request,"shop/prodList.html",{"Products":prods,"catname":cname})
    else:
        messages.warning(request,"No such category present !!")
        return redirect("collections")
    
    
def proddtls(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            prods=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/productdetails.html",{"Products":prods})
        else:
            messages.warning(request,"No such Product present !!")
            return redirect("Viewcollections")

    else:
        messages.warning(request,"No such category present !!")
        return redirect("collections")