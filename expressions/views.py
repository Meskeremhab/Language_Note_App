from rest_framework import generics, permissions, filters
from .models import Expression
from .serializers import ExpressionSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, "owner_id", None) == request.user.id

class ExpressionListCreate(generics.ListCreateAPIView):
    serializer_class = ExpressionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["text", "meaning", "region", "usage_notes"]
    ordering_fields = ["text", "created"]

    def get_queryset(self):
        return Expression.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ExpressionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpressionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Expression.objects.filter(owner=self.request.user)
