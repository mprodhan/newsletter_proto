from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=30)

    # The function allows for the representation of the name variable to appear
    # on the admin model site.
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
