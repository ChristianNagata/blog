from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Blog posts'

    def __str__(self) -> str:
        return self.text[:350] + ' [...]'
