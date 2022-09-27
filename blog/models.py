from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    status = models.IntegerField(default = 0)