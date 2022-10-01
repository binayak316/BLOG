from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="login-user"),
    path('register/', views.registerUser, name="register-user"),
    path('logout/', views.logoutUser, name="logout-user"),
    path('detail/<int:pk>/', views.detail, name="detail-view"),
    path('addblog/', views.addblog, name="add-blog"),
    path('profile/', views.profile, name='profile'),

    path('post_detail/<int:pk>', views.post_edit, name="blog-post-edit"),
    
]
