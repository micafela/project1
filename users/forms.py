from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


# custom user creation form

class CustomUserCreationFrom(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email',
                  'position', 'keywords',]
       # keyword = forms.CharField(label="enter muliple Words")
