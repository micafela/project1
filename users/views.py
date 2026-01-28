from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationFrom
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'index.html')

# register a user


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('users:home')
    else:
        form = CustomUserCreationFrom()

    return render(request, 'register.html', {'form': form})

# login


def login_view(request):
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            # log the user in
            login(request, form.get_user())

            return redirect('users:home')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# users home page
@login_required(login_url='/users/login/')
def home(request):

    return render(request, 'home.html')

# logout


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:login')
