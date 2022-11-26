from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Band(models.Model):
    band_name = models.CharField(_('name'), max_length=255)


# class Song(models.Model):
#     title = models.CharField(_('title'), max_length=100)
#     duration = models.CharField(_('duration'), max_length=5)
#     band_id = models.ForeignKey(Band, verbose_name=_('band_id'), on_delete=models.CASCADE)

# class Album(models.Model):
#     album_name = models.CharField(_('album_name'), max_length=255)
#     band_id = models.ForeignKey(Band, verbose_name=_("band"), on_delete=models.CASCADE)

class AlbumReview(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='post',
    )
    # album_id = models.ForeignKey()
    review = models.TextField(_('review'))
    score = models.CharField(_('score'), max_length=10, help_text='enter score from 1 till 10')

def __str__(self):
    return _("{user}").format(
        user = self.user,        
    )

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    album_review_id = models.ForeignKey(
        AlbumReview,
        verbose_name=_("album_review_id"),
        on_delete=models.CASCADE
        related_name='comments'
    )

    def __str__(self):
        return("Comment on {album_review_id} by {user}").format(
            album_review_id=self.album_review_id,
            user=self.user
        )
        user = self.user

# class AlbumReviewLike(models.Model):
#     user = models.ForeignKey(
#         User,
#         verbose_name=_('user'),
#         on_delete=models.CASCADE,
#         related_name='like',
#     )
#     album_review_id = models.ForeignKey("album_review", verbose_name=_("album_review_id"), on_delete=models.CASCADE)
