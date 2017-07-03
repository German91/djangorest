from django.db import models

# Create your models here.
class Bucketlist(models.Model):
    # Bucketlist's fields
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Bucketlist's object representation
    def __str__(self):
        return '{}'.format(self.name)
