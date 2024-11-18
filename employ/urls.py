from django.urls import path

from . import views

app_name = 'employ'

urlpatterns = [
    path('',views.home,name = 'index'),
    path('portfolio/',views.portfolio, name = 'portfolio'),
    path('service/',views.service, name = 'service'),
    path('starter/',views.starter, name = 'starter'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
]


















