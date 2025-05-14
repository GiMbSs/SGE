from django.urls import path

from .views import (SupplierCreateView, SupplierDeleteView,
                    SupplierListCreateAPIView, SupplierListView,
                    SupplierRetrieveUpdateDeleteAPIView, SupplierUpdateView)

urlpatterns = [
    path('suppliers/list/', SupplierListView.as_view(), name='supplier_list'),
    path(
        'suppliers/create/',
        SupplierCreateView.as_view(),
        name='supplier_create',
    ),
    path(
        'suppliers/update/<int:pk>/',
        SupplierUpdateView.as_view(),
        name='supplier_update',
    ),
    path(
        'suppliers/delete/<int:pk>/',
        SupplierDeleteView.as_view(),
        name='supplier_delete',
    ),
    path(
        'api/v1/suppliers/',
        SupplierListCreateAPIView.as_view(),
        name='supplier_list_create',
    ),
    path(
        'api/v1/suppliers/<int:pk>/',
        SupplierRetrieveUpdateDeleteAPIView.as_view(),
        name='supplier_retrieve_update_delete',
    ),
]
