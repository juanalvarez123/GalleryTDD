from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>/gallery/', views.get_portafolio, name='get_portafolio'),
    path('login/', views.login, name='login'),
    path('<int:user_id>', views.manage_user, name='manage_user'),
    path('<str:username>/gallery/<int:image_id>', views.manage_portafolio, name='manage_portafolio'),
    path('', views.index, name='index')
]
