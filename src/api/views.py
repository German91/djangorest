from django.shortcuts import render
from rest_framework import generics

from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
# Generic view which provides GET and POST methods
class CreateView(generics.ListCreateAPIView):
    # Define query and serializer class
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
