from django.urls import path
from . import views

urlpatterns = [
    path('',views.url),
    path('process_url_from_client', views.process_url_from_client)
]
