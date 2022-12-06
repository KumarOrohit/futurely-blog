from django.urls import path
from .views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, CommentCreateView, CommentUpdateView, \
    ShareBlogView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='blogcreate'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blogupdate'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blogdelete'),
    path('comment-create/<int:blog>', CommentCreateView.as_view(), name='commentcreate'),
    path('comment-update/<int:pk>', CommentUpdateView.as_view(), name='commentupdate'),
    path('comment-share/<int:pk>', ShareBlogView.as_view(), name='sharecomment'),
]
