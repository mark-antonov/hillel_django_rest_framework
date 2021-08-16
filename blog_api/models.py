from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=250)
    full_description = models.TextField(blank=True)
    user = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    posted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False)
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    moderated = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text
