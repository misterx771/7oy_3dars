from rest_framework.serializers import ModelSerializer
from .models import Article, Author, Book

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only = ['id']
        
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author_id'] = AuthorSerializer(instance.author).data
        
        return data
        
class ArticleSerializer(ModelSerializer): 
    class Meta:
        model = Article
        fileds = "__all__"
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author_id'] = AuthorSerializer(instance.author).data

        return data