from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def AllProducts(request):
    products = Product.objects.all()
    return render(request,'all_products.html',{'products':products})

@login_required(login_url="/")
def AddProduct(request):
    add_form = ProductForm()
    if request.method == 'POST':
        add_form = ProductForm(request.POST,request.FILES)
        if add_form.is_valid():
            add_form.save()
            return redirect('all_products')
    return render(request,'add_product.html',{'add_form':add_form})

@login_required(login_url="/")
def UpdateProduct(request,id):
    edit_product = Product.objects.get(id=id)
    edit_form = ProductForm(instance=edit_product)
    if request.method == 'POST':
        edit_form = ProductForm(request.POST,request.FILES,instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('all_products')
    return render(request,'add_product.html',{'edit_form':edit_form})

@login_required(login_url="/")
def DeleteProduct(request,id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    return redirect('all_products')
