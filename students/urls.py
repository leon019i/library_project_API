from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentListView.as_view(), name='students'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student detail')
]
