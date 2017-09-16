from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    template = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
