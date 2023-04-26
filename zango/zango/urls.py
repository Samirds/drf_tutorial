
from django.contrib import admin
from django.urls import path, include
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import ShowProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', views.applicationData),
    path('api/profile/', ShowProfile.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
