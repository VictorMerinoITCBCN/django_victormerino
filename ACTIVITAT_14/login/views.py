from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm , LoginForm

def home(request):
    user_id = request.session.get("user_id")

    user = {
        "name": "Guest"
    }
    if user_id: user = User.objects.get(id=user_id)

    context = {
        "user": user
    }
    return render(request, "index.html", context)

def login(request):
    form = LoginForm()
    context = {
        "form": form,
        "title": "Login"
    }

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            auth = User.objects.filter(email=email, password=password).exists()

            if auth: 
                request.session["user_id"] = User.objects.get(email=email, password=password).id
                return redirect("home")
            
    return render(request, "login.html", context)

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            request.session["user_id"] = User.objects.get(email=email, password=password).id
            return redirect("home") 

    context = {
        "form": form,
        "title": "Register"
    }
    return render(request, "login.html", context)

def logout(request):
    if "user_id" in request.session:
        del request.session["user_id"]
    return redirect("home")