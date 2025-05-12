from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from django.contrib.auth. mixins import LoginRequiredMixin
from django.contrib import messages
from . import forms
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(View):
    
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/home.html', {'posts':posts})

class PostDetailView(View):
    form_class = forms.CommentCreateForm
    
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return super().setup(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        post = self.post_instance
        comments = post.post_comments.filter(is_reply=False)
        return render(request, 'home/detail.html', {'post':post, 'comments':comments, 'form':form})
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        post = self.post_instance 
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Your comment submitted successfully', 'success')
        return redirect('home:post_detail', post.id, post.slug)
    
    
class PostDeleteView(LoginRequiredMixin, View):
    
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if request.user.id == post.user.id:
            post.delete()
            messages.success(request, 'Post deleted successfully', 'success')
        else:
            messages.error(request, "You can't delete this post", 'danger')
            
        return redirect('home:home')
    
class PostUpdateView(LoginRequiredMixin, View):
    
    form_class = forms.PostCreateUpdateForm
    
    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not request.user.id == post.user.id:
            messages.error(request, "You can't update this post", 'danger')
            return redirect('home:home')
        
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'home/update.html', {'form':form})
        
    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_slug = form.cleaned_data['body'][:20]
            new_post.slug = slugify(new_slug)
            new_post.save()
            messages.success(request, 'Post updated successfully', 'success')
            return redirect('home:post_detail', post.id, post.slug)
        
class PostCreateView(LoginRequiredMixin, View):

    form_class = forms.PostCreateUpdateForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, 'home/create.html', {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_slug = form.cleaned_data['body'][:20]
            new_post.slug = slugify(new_slug)
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'Post created successfully', 'success')
            return redirect('home:post_detail', new_post.id, new_post.slug)




