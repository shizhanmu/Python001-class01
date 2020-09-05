from django.urls import path
from . import views


urlpatterns = [
    path('', views.ranking, name='ranking'),
    path('<int:pid>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
