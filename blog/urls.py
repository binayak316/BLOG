from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="login-user"),
    path('register/', views.registerUser, name="register-user"),
    path('logout/', views.logoutUser, name="logout-user"),
    path('detail/<int:pk>/', views.detail, name="detail-view"),
    path('addblog/', views.addblog, name="add-blog"),
    path('profile/', views.profile, name='profile'),

    path('post_edit/<int:pk>', views.post_edit, name="blog-post-edit"),
    path('post_delete/<int:pk>', views.post_delete, name="blog-post-delete"),

    #class based views for forget password
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='blog/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name='password_reset_complete'),



    
]
