from django.db import models
from .customer import Customer

class Profile(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profilePicture')
    bio = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.customer}"