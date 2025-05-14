from django.urls import path

from .views import (OutflowCreateView, OutflowDetailView,
                    OutflowListCreateAPIView, OutflowListView,
                    OutflowRetrieveAPIView)

urlpatterns = [
    path('outflows/list/', OutflowListView.as_view(), name='outflow_list'),
    path(
        'outflows/create/', OutflowCreateView.as_view(), name='outflow_create'
    ),
    path(
        'outflows/detail/<int:pk>/',
        OutflowDetailView.as_view(),
        name='outflow_detail',
    ),
    path(
        'api/v1/outflows/',
        OutflowListCreateAPIView.as_view(),
        name='outflow-list-create-api-view',
    ),
    path(
        'api/v1/outflows/<int:pk>/',
        OutflowRetrieveAPIView.as_view(),
        name='outflow-retrieve-api-view',
    ),
]
