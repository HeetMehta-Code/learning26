from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.home),
    path('test1/',views.test1),
    path('test2/',views.test2),
    path('test3/',views.test3),
    path('contact/', views.contact),
    path('about/', views.aboutUs),
]