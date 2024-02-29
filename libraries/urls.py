from django.urls import path
from .views import LibrariesList, LibrariesDetail

urlpatterns = [

    path('', LibrariesList.as_view(), name=''),
    path('<int:pk>/', LibrariesDetail.as_view(), name='')
]
