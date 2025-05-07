from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def contact_view(request):
    if request.method == 'POST':
        return HttpResponse("Данные успешно отправлены!")
