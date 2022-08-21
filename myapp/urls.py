from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('home', views.index,name='home'),
    path('contact', views.contact,name='contact'),
    path('services', views.services,name='services'),
    path('image', views.image,name='image'),
    path('video', views.video,name='video'),
]