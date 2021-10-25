from django.conf import settings
from django.db import models
from clients.models import Customer
# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=40)
	description = models.TextField(blank=False, null=False,max_length=160)
	price = models.FloatField(default=1)
	image = models.ImageField(upload_to='images/', blank=True, null=True, default='static/img/pexels-wendy-wei-1190297.jpg')
	seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False, related_name='customer')
	avalaible = models.BooleanField(default=False)

	def __str__(self):
		return self.title


