from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_attribute=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image', 'publication_attribute']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog:blogs_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'publication_attribute']
    template_name = 'blog_form.html'

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blogs_list')
