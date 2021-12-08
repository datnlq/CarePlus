from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.views.generic import *
from .models import Topic, Post, Comment
from .forms import CreateCommentForm
import requests
from notifications.signals import notify
from django.http import HttpResponse


# Topic views

class TopicListView(LoginRequiredMixin,ListView):
    model = Topic  # <app>/<model>_<viewtype>.html
    template_name = 'forum/index.html'

    def get_context_data(self, **kwargs):
    
        context = super(TopicListView,self).get_context_data(**kwargs)
        if "search" in self.request.GET:
            search_term = self.request.GET["search"]
            context['topics'] = Topic.objects.filter(title__icontains=search_term)
        else:
            context['topics'] = Topic.objects.all()       

        context['count'] = Topic.objects.all().count()
        return context

class TopicDetailView(LoginRequiredMixin,DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        if "search" in self.request.GET:
            search_term = self.request.GET["search"]
            context['posts'] = Post.objects.filter(title__icontains=search_term)
        else:
            context['posts'] = Post.objects.filter(topic=self.kwargs.get('pk'))  
        context['count'] = Post.objects.all().count()
        return context

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'description']

    def form_valid(self, form):
        return super().form_valid(form)




class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    form_class = CreateCommentForm

    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        if "search" in self.request.GET:
            search_term = self.request.GET["search"]
            context['comments'] = Comment.objects.filter(body__icontains=search_term)
        else:
            context['comments'] = Comment.objects.filter(post=self.kwargs.get('pk'))
        context['form'] = CreateCommentForm(initial={'post': self.object, 'author': self.request.user})
        

        return context

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form,self.object)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, post):
        form.save()
        if self.request.user != post.author:
            notify.send(self.request.user, recipient=post.author,actor=self.request.user, verb='commented on your post',Description='commented on your post', target=post.author)        
        return super(PostDetailView, self).form_valid(form)

            
            


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = Topic.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
