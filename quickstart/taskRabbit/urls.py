from django.urls import path, include
from auth.views import LogoutView

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/logout/", LogoutView.as_view()),
    # path('api/users/', include('users.urls')),
    # path('api/', include('commerce.urls')),       
]
