from django.shortcuts import render
from rest_framework import generics, permissions

from .permissions import IsOwner
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
# Generic view which provides GET and POST methods
class CreateView(generics.ListCreateAPIView):
    # Define query and serializer class
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
