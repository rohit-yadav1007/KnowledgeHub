from django.urls import path
from .views import home, ArticleDetail, AddPost, UpdatePost, DeletePost

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    path('article/<int:pk>/remove/', DeletePost.as_view(), name='delete_post'),
]
