from django import forms
from .models import Order

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service_type', 'room_count', 'bathroom_count', 'address', 'order_date']