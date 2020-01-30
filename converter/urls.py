from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('num_to_english/<num>', views.convert, name='convert')
]