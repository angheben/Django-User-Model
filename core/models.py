from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), name='author', verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField(name='title', max_length=100)
    text = models.TextField(name='text', max_length=400)
