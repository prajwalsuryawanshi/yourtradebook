from django import forms
from .models import Trade
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['date_of_trade', 'script_name', 'trade_type', 'buying_price', 'selling_price', 'quantity']
        widgets = {
            'date_of_trade': forms.DateInput(attrs={'type': 'date'}),
        }
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
