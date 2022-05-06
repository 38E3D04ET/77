from django_filters import FilterSet, DateFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):
    dataCreation = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = {
            'author',
            'postCategory__name',
        }


#class PostFilter(FilterSet):
#    date = DateFromToRangeFilter()
#    class Meta:
#        model = Post
#        fields = {
#            'postCategory__name': ['icontains'],
#            'author__name': ['contains'],
#        }


