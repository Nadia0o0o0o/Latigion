from django.urls import path
from . import views

urlpatterns = [
    path('', views.social_home, name='social_home'),
    path('post/', views.post_list, name='post_list'),
    path('en_desarrollo/', views.plantilla_no_funciona, name='plantilla_no_funciona'),
]
