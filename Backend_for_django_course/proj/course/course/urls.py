from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include("mainapp.urls")),
    # path('', include("shop.urls", namespace="shop")),
    # path('', include("users.urls", namespace="users")),
    path('', include("products.urls", namespace="products")),
    path('admin/', admin.site.urls),
]
