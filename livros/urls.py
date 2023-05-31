from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<str:livro_id>/', views.editar, name='editar'),
    path('excluir/<str:livro_id>/', views.excluir, name='excluir'),
]
