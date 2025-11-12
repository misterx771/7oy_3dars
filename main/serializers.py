from rest_framework import serializers
from .models import Author, Book, Article


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.year = validated_data.get("year", instance.year)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    desc = serializers.CharField()
    price = serializers.IntegerField()
    published_year = serializers.IntegerField()
    author = serializers.IntegerField(write_only=True)
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        validated_data["author_id"] = validated_data.pop("author")
        
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.price = validated_data.get("price", instance.price)
        instance.published_year = validated_data.get("published_year", instance.published_year)
        instance.author_id = validated_data.get("author", instance.author_id)

        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["author"] = AuthorSerializer(instance.author).data
        
        return rep


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=120)
    content = serializers.CharField()
    author = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        validated_data["author_id"] = validated_data.pop("author")
        
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.author_id = validated_data.get("author", instance.author_id)

        instance.save()
        
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["author"] = AuthorSerializer(instance.author).data
        
        return rep
