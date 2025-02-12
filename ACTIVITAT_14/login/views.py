from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def home(request):
    return render(request, "index.html")

def login(request):
    form = UserForm()
    context = {
        "form": form,
        "title": "Login"
    }

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            auth = User.objects.filter(email=email, password=password).exists()

            if auth: return redirect("home")
            
    return render(request, "login.html", context)

def register(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home") 

    context = {
        "form": form,
        "title": "Register"
    }
    return render(request, "login.html", context)