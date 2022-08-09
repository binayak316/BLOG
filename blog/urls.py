from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="login-user"),
    path('register/', views.registerUser, name="register-user"),
    path('logout/', views.logoutUser, name="logout-user"),
    path('detail/', views.detail, name="detail-view"),
    path('addblog/', views.addblog, name="add-blog"),
    path('profile/', views.profile, name='profile'),
    # path('addprofile/', views.addprofile, name='add-profile')
]
