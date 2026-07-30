from django.forms import ModelForm
from .models import Customer, Order
import django.forms as forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_since']

        widgets = {
            'customer_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'customer_since' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
        }



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_reference', 'product_reference', 'order_number', 'order_date', 'quantity']

        widgets = {
            'customer_reference' : forms.Select(attrs={'class' : 'form-control'}),
            'product_reference' : forms.Select(attrs={'class' : 'form-control'}),
            'order_number' : forms.TextInput(attrs={'class' : 'form-control'}),
            'order_date' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
            'quantity' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'amount' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'gst' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'bill_amount' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }