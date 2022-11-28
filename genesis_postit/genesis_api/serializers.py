from rest_framework import serializers
from . import models

class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = models.AlbumReview
        fields = ('id', 'user', 'user_id', 'review', 'score')