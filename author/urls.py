from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_home, name='author_home'),
    path('dibujo/', views.dibujo, name='dibujo'),
    path('writer/', views.writer, name='writer'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('Herramientas_creativas/', views.herramientas_creativas, name='Herramientas_creativas'),
    path('blog/', views.blog, name='blog'),
    
]

