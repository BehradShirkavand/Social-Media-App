from django.urls import path
from . import views



app_name = 'accounts'
urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profile'),
    path('reset/', views.UserPasswordResetView.as_view(), name='reset_password'),
    path("reset/done", views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("confirm/<uidb64>/<token>/", views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('confirm/complete/', views.UserPasswordResetComplete.as_view(), name='password_reset_complete'),
    path("follow/<int:user_id>/", views.UserFollowView.as_view(), name="user_follow"),
    path("follow/<int:user_id>/", views.UserUnfollowView.as_view(), name="user_unfollow"),
    
    
]
