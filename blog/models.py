from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='DEFAULT VALUE')
    created_on = models.DateTimeField()

    def __str__(self):
        return self.title