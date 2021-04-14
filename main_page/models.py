from django.db import models


class Introduction(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(upload_to='static/logos')
    activation = models.BooleanField()

    def __str__(self):
        return self.title
