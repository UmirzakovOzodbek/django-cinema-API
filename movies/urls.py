from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views, api


urlpatterns = [
    path('movie/', views.MovieViewSet.as_view({'get': 'list'})),
    path('movie/<int:pk>', views.MovieViewSet.as_view({'get': 'retrieve'})),
    path('review/', views.ReviewCreateViewSet.as_view({'post': 'create'})),
    # path('review/<int:pk>/', views.ReviewDestroy.as_view({'post': 'create'})),
    path('rating/', views.AddStarRatingViewSet.as_view({'post': 'create'})),
    path('actors/', views.ActorsViewSet.as_view({'get': 'list'})),
    path('actors/<int:pk>/', views.ActorsViewSet.as_view({'get': 'retrieve'})),
]


# router = DefaultRouter()
# # router.register(r'actor-read', api.ActorReadOnly, basename='actor')
# router.register(r'actor-modelset', api.ActorModelViewSet, basename='actor')
# urlpatterns = router.urls
