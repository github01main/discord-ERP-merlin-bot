from django.urls import path
from . import views

urlpatterns = [
    # 1st landing page pattern.
    path('', views.home, name='home'),
    
    # 2nd category pattern..
    path('category/<str:pk>/', views.category, name='category'),
    
    # 3rd create_post pattern..
    path('category/3/createPost/', views.createPost, name='createPost'),
    
    # 4rd update_post pattern..
    path('category/3/updatePost/<str:pk>', views.updatePost, name='updatePost'),
    
    # 5rd delete_post pattern..
    path('category/3/deletePost/<str:pk>', views.deletePost, name='deletePost'),
    
    # 6rd post_item pattern..
    path('category/3/post/<str:pk>/', views.post, name='post'),
    
    # 7rd login pattern..
    path('category/5/login', views.loginPage, name='login'),
    
    # 8rd logout pattern..
    path('category/5/logout', views.logoutUser, name='logout'),
    
    # 9rd register pattern..
    path('category/5/register', views.registerPage, name='register'),
    
    # 10th contact pattern.
    path('contact/', views.contact, name='contact'),
]