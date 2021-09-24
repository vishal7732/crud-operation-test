from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def product(request):
    products = Product.objects.all()
    pro = {'products':products}
    return render(request, "register.html",pro)

def edit(request,id):
    products = Product.objects.get(id=id)
    cat = Category.objects.all()
    
    if request.method == "POST":
        
        cate = request.POST['cat_name']
        asw = Product.objects.get(id=id)
        asw = asw.Category
        products = Product.objects.filter(Category=asw)
        products.Category = cate
        products.update()
        
    
        
    pro = {'products':products,'cat':cat}
    return render(request, "edit.html",pro)