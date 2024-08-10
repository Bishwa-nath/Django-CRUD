from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")