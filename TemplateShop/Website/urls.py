from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('produtos/', views.produtos, name="produtos"),
    path('carrinho/', views.carrinho, name="carrinho"),
    path('teste/', views.teste, name="teste")
]