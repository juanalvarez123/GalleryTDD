from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('gallery.urls')),
    path('user/', include('user.urls')),
]
