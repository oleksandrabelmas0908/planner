from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def index(req):
    return render(template_name="index.html", request=req)


def registration_view(req):
    return render(template_name="registration.html", request=req)


def login_view(req):
    if req.method == 'POST':
        name = req.POST.get("login")
        password = req.POST.get("password")

        user = authenticate(username=name, password=password)
        if user is not None:
            login(req, user)
            print(f"User: {name} is login in")
        else:
            print(f"User is not login in")
            return render(template_name="login.html", request=req)

        return redirect('home')

    else:
        return render(template_name="login.html", request=req)