from django.shortcuts import render, redirect
from .models import *
from .forms import CustomerForm, OrderForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def All_Customer(request):
    customers = Customer.objects.all()
    return render(request,'customers/all_customers.html',{'customers' : customers})

@login_required(login_url="/")
def Add_Customer(request):
    add_form = CustomerForm()
    if request.method == 'POST':
        add_form = CustomerForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('all_customers')
    return render(request,'customers/add_customer.html',{'add_form' : add_form})

@login_required(login_url="/")
def Edit_Customer(request, id):
    customer = Customer.objects.get(id=id)
    edit_form = CustomerForm(instance=customer)
    if request.method == 'POST':
        edit_form = CustomerForm(request.POST, instance=customer)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('all_customers')
    return render(request,'customers/add_customer.html',{'edit_form' : edit_form})

@login_required(login_url="/")
def Delete_Customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('all_customers')


@login_required(login_url="/")
def All_Orders(request):
    orders = Order.objects.all()
    return render (request,'orders/all_orders.html',{'orders' : orders})

@login_required(login_url="/")
def Add_Order(request):
    add_form = OrderForm()

    if request.method == 'POST':
        product_reference = Product.objects.get(id=request.POST.get('product_reference'))
        amount = float(product_reference.price)*float(request.POST.get('quantity'))
        gst = (amount*float(product_reference.gst))/100
        bill_amount = amount + gst
        new_order = Order(
            customer_reference_id = request.POST.get('customer_reference'),
            product_reference_id = request.POST.get('product_reference'),
            order_number = request.POST.get('order_number'),
            order_date = request.POST.get('order_date'),
            quantity = request.POST.get('quantity'),
            amount = amount,
            gst = gst,
            bill_amount = bill_amount

        )
        new_order.save()
        return redirect('all_orders')
    return render (request,'orders/add_order.html',{'add_form' : add_form})


@login_required(login_url="/")
def Edit_Order(request, id):
    order = Order.objects.get(id=id)
    edit_form = OrderForm(instance=order)

    if request.method == 'POST':
        product_reference = Product.objects.get(id=request.POST.get('product_reference'))
        amount = float(product_reference.price)*float(request.POST.get('quantity'))
        gst = (amount*float(product_reference.gst))/100
        bill_amount = amount + gst

        order_filter = Order.objects.filter(id=id)
        order_filter.update(
            customer_reference_id = request.POST.get('customer_reference'),
            product_reference_id = request.POST.get('product_reference'),
            order_number = request.POST.get('order_number'),
            order_date = request.POST.get('order_date'),
            quantity = request.POST.get('quantity'),
            amount = amount,
            gst = gst,
            bill_amount = bill_amount
        )

        return redirect('all_orders')
    return render (request,'orders/add_order.html',{'edit_form' : edit_form})

@login_required(login_url="/")
def Delete_Order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('all_orders')
        

