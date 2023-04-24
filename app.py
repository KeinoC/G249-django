from django.shortcuts import render
from .models import User
from django import forms


def users_list(request):
    users = User.objects.all()
    # ... do something with the users data
    return render(request, 'users_list.html', {'users': users})


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age']

