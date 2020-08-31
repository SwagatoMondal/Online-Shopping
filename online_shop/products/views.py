from django.shortcuts import render
from .models import User


# Create your views here.
def first(request):
    return render(request, 'page1.html')


def second(request):
    return render(request, 'page2.html')


def registration(request):
    if request.method == 'POST':
        u_dict = request.POST
        user = User(name=u_dict['name'], email=u_dict['email'], password=u_dict['password'])
        user.save()
    return render(request, 'registration.html')
