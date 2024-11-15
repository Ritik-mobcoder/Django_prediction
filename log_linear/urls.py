from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('logistic/', views.logistic_view, name='logistic'),
    path('regression/', views.regression_view, name='regression'),
    path('titanic', views.titanic, name='titanic'),
    path('expirence', views.expirence, name='expirence'),
    
]