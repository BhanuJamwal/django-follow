from django.contrib.auth.models import User
from django.db import models

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers',on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def save(self, **kwargs):
        """
        A mostly-generic save method, except that it validates that the user
        is not attempting to follow themselves.
        """
        if self.follower == self.following:
            raise ValueError("Cannot follow yourself.")
        super(Follower, self).save(**kwargs)

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)