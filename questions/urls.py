from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('practice', views.practice, name='practice'),
    path('result', views.result, name='result'),
]
