from django.urls import path

from .views import (InflowCreateView, InflowDetailView,
                    InflowListCreateAPIView, InflowListView,
                    InflowRetrieveAPIView)

urlpatterns = [
    path('inflows/list/', InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', InflowCreateView.as_view(), name='inflow_create'),
    path(
        'inflows/detail/<int:pk>/',
        InflowDetailView.as_view(),
        name='inflow_detail',
    ),
    path(
        'api/v1/inflows/',
        InflowListCreateAPIView.as_view(),
        name='inflow-list-create-api-view',
    ),
    path(
        'api/v1/inflows/<int:pk>/',
        InflowRetrieveAPIView.as_view(),
        name='inflow-retrieve-api-view',
    ),
]
