from django.urls import path
from app.views import my_view

urlpatterns = [
    path('myapp/', my_view, name='my_view'),
]
