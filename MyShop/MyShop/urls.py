from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
]
