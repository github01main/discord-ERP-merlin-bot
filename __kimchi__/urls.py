from django.urls import path
from . import views

urlpatterns = [
    # 1st landing page pattern.
    path('', views.home, name='home'),
    # 2nd document pattern..
    path('document/<str:pk>/', views.document_page, name='document'),
    # 3rd post_item pattern..
    path('post_item/<str:pk>/', views.Post_item, name='post_item'),
    # 4th contact pattern.
    path('contact/', views.contact, name='contact'),
]