from django.shortcuts import render

# Create your views here.


def base(request, name):
    return render(request, 'app/main.html', {'name': name})
