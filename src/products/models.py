from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=40)
	description = models.TextField(blank=False, null=False,max_length=160)
	price = models.FloatField(default=1)
	image = models.ImageField(upload_to='images/', blank=True, null=True)
	avalaible = models.BooleanField(default=False)

	def __str__(self):
		return self.title