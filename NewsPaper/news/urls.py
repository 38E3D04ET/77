from django.urls import path
from .views import PostList, PostDetail, SearchList

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', SearchList.as_view()),
]
