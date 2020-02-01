from django.urls import path
from . import views

urlpatterns = [
    path('num_to_english/<number>', views.convert, name='convert')
]