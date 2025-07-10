from django.contrib import admin
from django.http import JsonResponse

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
def health_check(request):
    return JsonResponse({"status": "API running 🚀"})
urlpatterns = [
    path('', health_check),
    path('admin/', admin.site.urls),
    path('api/', include('editor.urls')),  # Your app's urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
