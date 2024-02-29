from msilib.schema import ListView

from django.shortcuts import render
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer
from rest_framework.response import Response


# Create your views here.

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Student created successfully'})


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'message': 'Student updated successfully'})

    def delete(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')  # Get the ID of the student being deleted
        response = super().delete(request, *args, **kwargs)
        return Response({'message': f'Student with ID {student_id} deleted successfully'})