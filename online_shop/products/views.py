from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from .models import User


# Create your views here.
def first(request):
    if request.method == 'POST':
        u_dict = request.POST
        try:
            user = User.objects.get(email=u_dict['email'], password=u_dict['password'])
            if user is None:
                raise Http404("User does not exist")
        except User.DoesNotExist:
            raise Http404("User does not exist")
        else:
            return second(request, name=user.name)
    return render(request, 'page1.html')


def second(request, name='Guest'):
    context = {"name": name}
    return render(request, 'page2.html', context)


def registration(request):
    if request.method == 'POST':
        u_dict = request.POST
        user = User(name=u_dict['name'], email=u_dict['email'], password=u_dict['password'])
        user.save()
        return second(request, name=user.name)
    return render(request, 'registration.html')


def users_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = User.objects.all()

    return render(request, "users.html", context)
