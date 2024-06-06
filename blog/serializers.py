from rest_framework import serializers
from . models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class BlogSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'category_id', 'category']
    
   