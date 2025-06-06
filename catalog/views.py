from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Contact, Product


# Create your views here.
def main_view(request):
    return render(request, 'main.html')


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ContactView(View):
    def post(self, request):
        return HttpResponse("Данные успешно отправлены!")


class HomeViewListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.order_by('-created_at')[:5]
        return context


class ContactListListView(ListView):
    model = Contact
    template_name = 'contacts.html'
    context_object_name = 'contacts'
    queryset = Contact.objects.all()


class ProductListListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductDetailDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:products_list')
