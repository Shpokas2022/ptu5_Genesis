from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
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

class AlbumReviewLikeCreate(generics, mixins.DestroyModelMixin):
    serializers_class = serializers.AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        review = models.ReviewLike.objects.get(pk=self.kwargs['pk'])
        return models.ReviewLike.objects.filter(user=user, review=review)

    def perform_create(self, serializer):
        if self.get_queryset().exists:
            raise ValidationError(_("You can't like post more, then one time"))
        user = self.request.user
        review = models.AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=user, review=review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError(_('You do not like this post to begin with'))
