from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)


urlpatterns = [
    path('', views.users, name="users-list"),
    path('profile/<str:pk>/', views.user, name="single-user"),
    path('my-account/', views.myAccount, name="my-account"),
    path('update-profile/', views.updateProfile, name="update-profile"),
    path('skill/add/', views.addSkill, name="add-skill"),
    path('skill/edit/<str:pk>/', views.editSkill, name="edit-skill"),
    path('skill/delete/<str:pk>/', views.deleteSkill, name="delete-skill"),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.singleMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
    path('login/', auth_views.LoginView.as_view(
        redirect_authenticated_user=True), name='login'),
    path("logout", LogoutView.as_view(), name='logout'),
    path('update-password/',
         PasswordChangeView.as_view(), name="update-password"),
    path('password_change_done/', PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path("register/", views.register, name='register'),
    path("reset-password/", PasswordResetView.as_view(), name='reset-password'),
    path("password-reset-done/", PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
