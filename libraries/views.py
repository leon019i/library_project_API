from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from .models import LibraryMember

from .serializers import LibrarySerializer


# Create your views here.

class LibrariesList(generics.ListCreateAPIView):
    # LibraryMember.generate_fake_data()
    queryset = LibraryMember.objects.all()
    serializer_class = LibrarySerializer


class LibrariesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryMember.objects.all()
    serializer_class = LibrarySerializer

    def update(self, request, *args, **kwargs):
        id = kwargs.get('id')
        return Response({'message': f'Id: {id} ', 'id': id}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        return Response({'message': f'Id: {id} Updated successfully', 'id': id}, status=status.HTTP_204_NO_CONTENT)
