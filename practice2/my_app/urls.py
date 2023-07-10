from my_app import views
from django.urls import path

app_name = 'my_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
]
