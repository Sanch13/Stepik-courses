from django.urls import path

from . import views


app_name = "products"

urlpatterns = [
    path('goods/', views.list_goods, name='goods'),  # ?token=<uuid:token>
    path('new_good/', views.NewGoodAPI.as_view(), name='new_good'),
    path('get_token/', views.get_token, name='get_token'),
]
