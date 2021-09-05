from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    
    
    
