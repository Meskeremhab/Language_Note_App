from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Deck(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="decks")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = [("user", "name")]
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Word(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='words')
    deck = models.ForeignKey('vocab.Deck', on_delete=models.CASCADE, related_name='words')
    term = models.CharField(max_length=120)
    translation = models.CharField(max_length=120, blank=True)
    example = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='words', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('owner', 'deck', 'term')
        ordering = ['term']

    def __str__(self):
        return self.term
