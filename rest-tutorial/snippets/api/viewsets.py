from snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

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

    @action(methods=['get'],detail=False)
    def newest(self,request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)




