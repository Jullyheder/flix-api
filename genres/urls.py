from genres import views
from django.urls import path


urlpatterns = [
    path('', views.genre_create_list_view, name='genre-create-list'),
    path('<int:pk>/', views.genre_detail_view, name='genre-detail'),
]
