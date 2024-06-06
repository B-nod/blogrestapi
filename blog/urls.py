from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogListCreate.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogRetrieveUpdate.as_view(), name='blogupdate'),
    path('categories/', CategoryListCreate.as_view(), name='categories'),
    path('categories/<int:pk>/',CategoryRetrieveUpdate.as_view(), name='categoryupdate')
]