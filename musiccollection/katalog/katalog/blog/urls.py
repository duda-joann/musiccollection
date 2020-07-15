from django.urls import path
from .views import PostViewList, UpdatePost, CreatePost, DeletePost

app_name = 'blog'

urlpatterns = [
    path('blog', PostViewList.as_view(), name='post general'),
    path('editpost/<title>', UpdatePost.as_view(), name='edit post'),
    path('createpost', CreatePost.as_view(), name = 'create post'),
    path('deletepost', DeletePost.as_view(), name = 'delete post'),
]
