from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('themodel/', views.TheModelView, name= 'TheModelView'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    ]