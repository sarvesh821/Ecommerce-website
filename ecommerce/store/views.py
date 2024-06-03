from django.shortcuts import render,redirect
from .models import Product,Category
# Create your views here.
from django.contrib import messages
def homePage(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})



def about(request):
	return render(request, 'about.html', {})

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def category(request,foo):
    foo=foo.replace('-',' ')
    try:
          category=Category.objects.get(name=foo)
          products=Product.objects.filter(category=category)
          return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,"This category does not exists")
        return redirect('home')



     