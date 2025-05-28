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
    products = Product.objects.all()
    latest_products = Product.objects.order_by('-created_at')[:5]
    context = {'latest_products': latest_products,
               'products': products}
    return render(request, 'home.html', context)


def contact_list(request):
    contactss = Contact.objects.all()
    context = {'contacts': contactss}
    return render(request, 'contacts.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
