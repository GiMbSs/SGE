from django.urls import path

from .views import (CategoryCreateListAPIView, CategoryCreateView,
                    CategoryDeleteView, CategoryListView,
                    CategoryRetrieveUpdateDeleteAPIView, CategoryUpdateView)

urlpatterns = [
    path('categories/list/', CategoryListView.as_view(), name='category_list'),
    path(
        'categories/create/',
        CategoryCreateView.as_view(),
        name='category_create',
    ),
    path(
        'categories/update/<int:pk>/',
        CategoryUpdateView.as_view(),
        name='category_update',
    ),
    path(
        'categories/delete/<int:pk>/',
        CategoryDeleteView.as_view(),
        name='category_delete',
    ),
    path(
        'api/v1/categories/',
        CategoryCreateListAPIView.as_view(),
        name='category-create-list-api-view',
    ),
    path(
        'api/v1/categories/<int:pk>/',
        CategoryRetrieveUpdateDeleteAPIView.as_view(),
        name='category-retrieve-update-delete-api-view',
    ),
]
