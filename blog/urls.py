from django.urls import path
from blog import views

urlpatterns = [
    path('index/<int:id>/', views.index),
    path('access/<int:age>/', views.access),
]
