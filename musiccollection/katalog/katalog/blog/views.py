from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm


# Create your views here.


class PostViewList(ListView):
    template_name = 'blog\main.html'
    model = Post
    paginate_by = 10
    ordering = ['-published_date']
    context_object_name = 'posts'


class CreatePost(CreateView):
    template_name = 'blog/new_post.html'
    form_class = PostForm


class UpdatePost(UpdateView):
    template_name = 'blog/update_post.html'
    form_class = PostForm
    success_url = '/posts/'

    def get_object(self, queryset=None):
        object_to_update = Post.objects.get(title=self.kwargs['title'])
        return object_to_update


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog\delete_post.html'

    def get_object(self, queryset=None):
        object_to_update = Post.objects.get(title=self.kwargs['title'])
        return object_to_update
