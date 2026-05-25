from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def nameRef(request):

    if request.method == "POST":

        name = request.POST.get("name")

        if not name:
            return HttpResponse("Please enter your name.")

        name1 = name.lower()

        if "script" in name1:

            name2 = name1.replace("script", "")

            return HttpResponse(name2)

        else:
            return HttpResponse(name1)

    else:
        return HttpResponse("Please Enter your name.")