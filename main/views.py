from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Tasks


def index(req):
    print(User.objects.all())
    return render(template_name="index.html", request=req)


def registration_view(req):
    if req.method == 'POST':
        name = req.POST.get("login")
        password = req.POST.get("password")
        password2 = req.POST.get("password2")

        if password == password2:
            User.objects.create_user(username=name, password=password)
            user = authenticate(username=name, password=password)
            if user is not None:
                login(req, user)
            else:
                return render(template_name="login.html", request=req)

            return redirect('home')

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
        print("fsjkd;l")
        return render(template_name="login.html", request=req)


@login_required
def home(req):
    tasks = Tasks.objects.filter(user=req.user)
    print(tasks)
    return render(req, 'home.html', context={"tasks": tasks, "user": req.user})


@login_required
def add_task(req):
    if req.method == 'POST':
        task_name = req.POST.get("name")
        time_it_takes = req.POST.get("time_it_takes")
        user = req.user

        new_task = Tasks(user=user, title=task_name, time_it_takes=time_it_takes)
        new_task.save()

        return redirect('home')

    return render(req, 'add_task.html')
