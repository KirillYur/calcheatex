from django.urls import include,path
from . import views


urlpatterns = [
    path('calculation', views.calc),
    path('', views.base, name='base'),
    path('types/<slug:types_id>/', views.types),
]