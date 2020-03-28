from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>/gallery/', views.get_portafolio, name='get_portafolio'),
    path('login/', views.login, name='login')
]
