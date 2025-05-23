from django.shortcuts import render, redirect
from django.views import View 
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
#from home.models import Post   because we use related_name in Post model
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import Relation


class UserRegisterView(View):
    
    form_class = forms.UserRegistrationForm
    template_name = 'accounts/register.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'User registered successfully', 'success')
            return redirect('home:home')
        
        return render(request, self.template_name, {'form':form})
    
    
class UserLoginView(View):
    
    form_class = forms.UserLoginForm
    template_name = 'accounts/login.html'
    
    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
    
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'User logged in successfully', 'success')
                if self.next:
                    return redirect(self.next)
                
                return redirect('home:home')
            
            messages.error(request, 'Username or password is incorrect', 'danger')
        
        form = forms.UserLoginForm()
        return render(request, self.template_name, {'form': form})
    
    
class UserLogoutView(LoginRequiredMixin, View):
    
    def get(self, request):
        logout(request)
        messages.success(request, 'User logged out successfully')
        return redirect('home:home')
    
    
class UserProfileView(LoginRequiredMixin, View):
    
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        posts = user.posts.all()
        return render(request, 'accounts/profile.html', {'user':user, 'posts':posts})
        
        
class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'
    
class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'
    
class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm_form.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    
class UserPasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
    
    
class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user  = User.objects.get(pk=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            messages.error(request, 'You are already following this user', 'danger')
        else:
            Relation.objects.create(from_user=request.user, to_user=user)
            messages.success(request, 'You followed this user successfully', 'success')
            
        return redirect('accounts:profile', user.id)
            
            
class UserUnfollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user  = User.objects.get(pk=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            relation.delete()
            messages.success(request, 'You unfollowed this user', 'success')
        else:
            messages.error(request, 'You are not following this user', 'danger')
            
        return redirect('accounts:profile', user.id)
    
    
    
    