from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
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


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.user != request.user:
            return HttpResponseForbidden("У вас нет прав на редактирование этого продукта.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if not (product.user == request.user or request.user.has_perm('catalog.delete_product')):
            return HttpResponseForbidden("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)


@login_required
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def unpublish_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.publication_attribute = False
    product.save()
    return redirect('catalog:product_detail', product_id=product.id)
