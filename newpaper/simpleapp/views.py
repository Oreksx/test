from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from news.models import Post, Category
from django.core.paginator import Paginator
from .filters import NewFilter
from simpleapp.forms import NewForm

class NewList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-datepost']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET,queryset=self.get_queryset())
        return context

class NewDetailView(DetailView):
    template_name = 'new_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'news'

class NewCreateView(CreateView):
    template_name = 'new_create.html'
    form_class = NewForm

class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET,queryset=self.get_queryset())
        return context
    
class NewUpdateView(UpdateView):
    template_name = 'new_create.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    
class NewDeleteView(DeleteView):
    template_name = 'new_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'news'
































