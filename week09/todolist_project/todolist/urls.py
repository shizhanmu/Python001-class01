from django.urls import path

from . import views as main_views

urlpatterns = [
    path('loadme/', main_views.loadme, name='loadme')
]