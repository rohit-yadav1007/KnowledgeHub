from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatePost.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')
