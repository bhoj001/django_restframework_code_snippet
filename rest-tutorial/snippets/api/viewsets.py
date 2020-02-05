from snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from django_filters import rest_framework as filters 


# lets create a filter for django queryset
# This helps to filter by any text match in title i.e icontain not exact match
# We may have to replace exact title match with this icontains match
class SnippetFilter(filters.FilterSet):
    # title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Snippet
        # fields=('title','created')
        # Note if we only want to change look up expression then we can do
        # like this:
        # Note: iexact= exact match, lte= less than or equal to , gte = greater than or equal to 
        fields  = {
            'title':['icontains'],
            'created':['iexact','lte', 'gte']

        }


# # Lets implement below class with our own function for retrive, list, create and so on
# # note: we are inheriting from viewset class now not ModelViewSet as we did before
# class SnippetViewSet(viewsets.ViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


#     def list(self,request):
#         serializer = self.serializer_class(self.queryset,many=True)
#         return Response(serializer.data)


class SnippetViewSet(viewsets.ModelViewSet):
    #   we already get these methods(list,create, retrive, update, partial_update, destroy ) 
    #   so we don't have to implement it by ourself
    #   but if we use ViewSet class we do have to implement it 
    #  list,create, retrive, update, partial_update, destroy => already available
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # Instead of defining token based authentication and permission in settings.py we can also
    # set those setting here using AUTHENTICATION_CLASSES AND PERMISSION_CLASSES
    # ---There below are the two code 
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # Applying filter to django 
    # filter_fields = ('title','created')
    filterset_class = SnippetFilter


    @action(methods=['get'],detail=False)
    def newest(self,request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
    

    # def get_queryset(self):
    #     return Snippet.objects.filter(title__icontains='h1')


