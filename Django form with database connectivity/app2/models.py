from django.db import models

# Create your models here.
class formpage(models.Model):
    name = models.CharField(max_length = 250)
    phone = models.CharField(max_length=10, unique = True)
    email = models.EmailField(max_length = 250, unique = True)
    comment = models.TextField()

    def __str__(self):
        return self.name
