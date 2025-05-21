from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Contact, Product

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def contact_view(request):
    if request.method == 'POST':
        return HttpResponse("Данные успешно отправлены!")


def home_view(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    context = {'latest_products': latest_products}
    return render(request, 'home.html', context)


def contact_list(request):
    contactss = Contact.objects.all()
    context = {'contacts': contactss}
    return render(request, 'contacts.html', context)
