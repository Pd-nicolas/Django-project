from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro-cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('reserva/', views.reserva, name='reserva'),
    path('delivery/', views.delivery, name='delivery'),
    path('cardapio/', views.cardapio, name='cardapio'),
    path('delivery/<int:pedido_id>/confirmar/', views.confirmar_delivery, name='confirmar_delivery'),
    path('admin/', admin.site.urls),
]
