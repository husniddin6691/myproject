from django import forms
from django.contrib.auth import get_user_model

Account = get_user_model()

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'role'] 
