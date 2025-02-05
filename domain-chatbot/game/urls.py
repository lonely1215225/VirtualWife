from django.urls import path

from . import views

urlpatterns = [
    path('create_competition', views.create_competition_req, name='create_competition'),
    path('start_game', views.start_game, name='start_game'),
    path('image/<str:image_name>/', views.serve_image, name='serve_image'),
]
