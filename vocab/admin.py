from django.contrib import admin
from .models import Deck, Word, Tag

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'id')
    search_fields = ('name', 'user__username')

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('term', 'deck', 'owner', 'updated')
    list_filter = ('deck', 'tags')
    search_fields = ('term', 'translation', 'example', 'notes')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
