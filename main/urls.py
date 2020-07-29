from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('<int:id>/', views.reserve, name='reserve'),
    path('add', views.addevent, name='add'),
]