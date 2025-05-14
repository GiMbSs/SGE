from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path(
        'api/v1/authentication/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'api/v1/authentication/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path(
        'api/v1/authentication/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify',
    ),
]
