from django.shortcuts import render


# Create your views here.
def first(request):
    return render(request, 'page1.html')


def second(request):
    return render(request, 'page2.html')
