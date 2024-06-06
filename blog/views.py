from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializers import *

# Create your views here.
class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer

    def perform_create(self, serializer):
        category_id = self.request.data.get('category_id')
        category = Category.objects.get(id=category_id)
        serializer.save(category=category)


class BlogRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer

    def perform_update(self, serializer):
        category_id = self.request.data.get('category_id')
        if category_id:
            category = Category.objects.get(id=category_id)
            serializer.save(category=category)
        else:
            serializer.save()

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
