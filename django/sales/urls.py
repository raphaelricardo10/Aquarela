from django.urls import path
from sales import views

urlpatterns = [
    path('', views.SalesView.as_view(), name='sales'),
]