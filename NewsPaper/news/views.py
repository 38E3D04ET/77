from datetime import datetime
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm
from .models import Post, Category


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    ordering = ['-dataCreation']
#    queryset = Post.objects.order_by('-dataCreation')
    paginate_by = 3

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        context['posts'] = Post.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)

    def __str__(self):
        return f'{self.author}: {self.postTitle}'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

    queryset = Post.objects.all()

class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-dataCreation']
    paginate_by = 20

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }

