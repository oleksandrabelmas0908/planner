from django.shortcuts import render



def index(req):
    return render(template_name="index.html", request=req)


