from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_contacts),
    path('message/', views.send_message),
]