from django.urls import path

from .views import (ProductCreateView, ProductDeleteView, ProductDetailView,
                    ProductListCreateAPIView, ProductListView,
                    ProductRetrieveUpdateDeleteAPIView, ProductUpdateView)

urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='product_list'),
    path(
        'products/create/', ProductCreateView.as_view(), name='product_create'
    ),
    path(
        'products/detail/<int:pk>/',
        ProductDetailView.as_view(),
        name='product_detail',
    ),
    path(
        'products/update/<int:pk>/',
        ProductUpdateView.as_view(),
        name='product_update',
    ),
    path(
        'products/delete/<int:pk>/',
        ProductDeleteView.as_view(),
        name='product_delete',
    ),
    path(
        'api/v1/products/',
        ProductListCreateAPIView.as_view(),
        name='product-list-create-api-view',
    ),
    path(
        'api/v1/products/<int:pk>/',
        ProductRetrieveUpdateDeleteAPIView.as_view(),
        name='product-retrieve-update-delete-api-view',
    ),
]
