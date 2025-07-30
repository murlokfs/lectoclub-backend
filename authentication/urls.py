from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    register_view,
    logout_view,
    UserProfileView,
    user_profile_view,
)

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('me/', user_profile_view, name='user_me'),
]
