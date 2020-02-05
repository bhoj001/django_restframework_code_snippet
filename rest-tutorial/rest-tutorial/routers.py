from snippets.api.viewsets import SnippetViewSet
from rest_framework import routers


router = routers.DefaultRouter()
# router uses basename to figure out the name of the url
router.register('snippets',SnippetViewSet, basename='snippet')


# for url in router.urls:
#     print(url , '\n')
