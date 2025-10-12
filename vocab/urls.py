from django.urls import path
from .views import (
    DeckListCreate, DeckDetail,
    WordListCreate, WordDetail,
    TagListCreate,
)

urlpatterns = [
    path('decks/', DeckListCreate.as_view(), name='deck-list'),
    path('decks/<int:pk>/', DeckDetail.as_view(), name='deck-detail'),

    # words (nested by deck OR flat)
    path('decks/<int:deck_id>/words/', WordListCreate.as_view(), name='deck-words'),
    path('words/', WordListCreate.as_view(), name='word-list'),
    path('words/<int:pk>/', WordDetail.as_view(), name='word-detail'),

    # tags
    path('tags/', TagListCreate.as_view(), name='tag-list'),
]
