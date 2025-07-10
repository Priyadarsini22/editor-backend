from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, RegisterView, UserView, PublicDocumentView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='user'),
    path('public-documents/<int:pk>/', PublicDocumentView.as_view(), name='public_doc'),
]
