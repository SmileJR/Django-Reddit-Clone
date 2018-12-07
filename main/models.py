from django.db import models


class Post(models.Model):
    created_at: models.DateField()
    title = models.CharField(max_length=255)
    picture = models.TextField()
    content = models.TextField()
    site_url = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateField()
    content = models.TextField()
    vote_total = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
