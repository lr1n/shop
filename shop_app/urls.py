from django.urls import path, include
from .views import (IndexView,
                    ItemListView,
                    ItemCreate,
                    ItemDetail,
                    ItemUpdate,
                    ItemDelete,
                    ShopListView,
                    ShopCreate,
                    ShopDetail,
                    ShopUpdate,
                    ShopDelete)

app_name = 'shop_app'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('item_list/', ItemListView.as_view(), name='item_list'),
    path('item_create/', ItemCreate.as_view(), name='item_create'),
    path('item_detail/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('item_update/<int:pk>/', ItemUpdate.as_view(), name='item_update'),
    path('item_delete/<int:pk>/', ItemDelete.as_view(), name='item_delete'),
    path('api/', include('shop_app.api.urls')),
    path('shop_list/', ShopListView.as_view(), name='shop_list'),
    path('shop_create/', ShopCreate.as_view(), name='shop_create'),
    path('shop_detail/<int:pk>/', ShopDetail.as_view(), name='shop_detail'),
    path('shop_update/<int:pk>/', ShopUpdate.as_view(), name='shop_update'),
    path('shop_delete/<int:pk>/', ShopDelete.as_view(), name='shop_delete'),
]
