from django.shortcuts import render
from rest_framework import generics, permissions
from . import models, serializers

class AlbumReviewList(generics.ListAPIView):
    queryset = models.AlbumReview.objects.all()
    serializer_class = serializers.AlbumReviewSerializer

    def perform_create(self, serializer):
        serializer.safe(user=self.request.user)

class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AlbumReview.objects.all()
    serializer_class = serializers.AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
