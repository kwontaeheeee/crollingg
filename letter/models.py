from django.db import models

# Create your models here.
class Letter(models.Model) :
    user = models.ForeignKey
    title = models.CharField(max_length=100)
    write = models.CharField(max_length=100)
    contents = models.TextField(blank=True)
    send = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
