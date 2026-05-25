from django.shortcuts import render
from django.http import HttpResponse
import html


def index(request):
    return render(request, 'index.html')


def nameRef(request):

    if request.method == "POST":

        name = request.POST.get("name")

        if not name:
            return HttpResponse("Please enter your name.")

        # Vulnerable Output
        vulnerable_output = f"""
        <h2>Vulnerable Output:</h2>
        Hello {name}
        """

        # Secure Output
        safe_name = html.escape(name)

        secure_output = f"""
        <h2>Secure Output:</h2>
        Hello {safe_name}
        """

        return HttpResponse(vulnerable_output + "<hr>" + secure_output)

    return HttpResponse("Invalid Request")