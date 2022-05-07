from django.db import models


class Post(models.Model):  # new
    text = models.TextField()