from rest_framework import serializers
from .models import Deck, Word, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class DeckSerializer(serializers.ModelSerializer):
    # read-only: you won’t send this from the client
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Deck
        fields = ["id", "name", "description", "user"]

class WordSerializer(serializers.ModelSerializer):
    # nested tag objects: [{ "name": "Travel" }]
    tags = TagSerializer(many=True, required=False)
    deck_name = serializers.ReadOnlyField(source="deck.name")

    class Meta:
        model = Word
        fields = [
            "id", "term", "translation", "example", "notes",
            "deck", "deck_name", "tags", "created", "updated",
        ]
        read_only_fields = ["created", "updated"]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags", [])
        word = Word.objects.create(**validated_data)
        for t in tags_data:
            tag, _ = Tag.objects.get_or_create(name=t["name"])
            word.tags.add(tag)
        return word

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags", None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        if tags_data is not None:
            instance.tags.clear()
            for t in tags_data:
                tag, _ = Tag.objects.get_or_create(name=t["name"])
                instance.tags.add(tag)
        return instance
