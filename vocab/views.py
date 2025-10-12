from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Deck, Word, Tag
from .serializers import DeckSerializer, WordSerializer, TagSerializer

class IsOwner(permissions.BasePermission):
    """Object-level permission: only the owner can access the object."""
    def has_object_permission(self, request, view, obj):
        # Deck has `user`; Word has `owner`; handle both safely
        owner_id = getattr(obj, "owner_id", None) or getattr(obj, "user_id", None)
        return owner_id == request.user.id

# ---- Decks ----
class DeckListCreate(generics.ListCreateAPIView):
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["name"]

    def get_queryset(self):
        # Only the current user's decks, with word count (handy for UI)
        return Deck.objects.filter(user=self.request.user).annotate(words_count=Count("words"))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeckDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user)

# ---- Words ----
class WordListCreate(generics.ListCreateAPIView):
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["term", "translation", "example", "notes"]
    ordering_fields = ["term", "updated", "created"]

    def get_queryset(self):
        qs = Word.objects.filter(owner=self.request.user).select_related("deck").prefetch_related("tags")
        deck_id = self.kwargs.get("deck_id")
        if deck_id:
            qs = qs.filter(deck_id=deck_id)
        return qs

    def perform_create(self, serializer):
        deck_id = self.kwargs.get("deck_id") or self.request.data.get("deck")
        serializer.save(owner=self.request.user, deck_id=deck_id)

class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Word.objects.filter(owner=self.request.user)

# ---- Tags ----
class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
