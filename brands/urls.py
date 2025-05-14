from django.urls import path

from .views import (BrandCreateListAPIView, BrandCreateView, BrandDeleteView,
                    BrandListView, BrandRetrieveUpdateDeleteAPIView,
                    BrandUpdateView)

urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name='brand_list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
    path(
        'brands/update/<int:pk>/',
        BrandUpdateView.as_view(),
        name='brand_update',
    ),
    path(
        'brands/delete/<int:pk>/',
        BrandDeleteView.as_view(),
        name='brand_delete',
    ),
    path(
        'api/v1/brands/',
        BrandCreateListAPIView.as_view(),
        name='brand-create-list-api-view',
    ),
    path(
        'api/v1/brands/<int:pk>/',
        BrandRetrieveUpdateDeleteAPIView.as_view(),
        name='brand-retrieve-update-delete-api-view',
    ),
]
