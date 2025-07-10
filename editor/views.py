# editor/views.py
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Document
from .serializers import UserSerializer, RegisterSerializer, DocumentSerializer

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# User Info View
class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# Document ViewSet
class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user) | Document.objects.filter(is_public=True)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# NEW: Public single document view
class PublicDocumentView(generics.RetrieveAPIView):
    queryset = Document.objects.filter(is_public=True)
    serializer_class = DocumentSerializer
    permission_classes = []  # allow anyone to view
