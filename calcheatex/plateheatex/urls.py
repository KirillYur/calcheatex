from django.urls import path
from . import views

urlpatterns = [
    path('calculation', views.calc),
    path('', views.index),
    path('types/<slug:types_id>/', views.types),
]