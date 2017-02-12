from django.db import models

# Create your models here.
class Factura(models.Model):
	"""docstring for ClassName"""
	nombre = models.CharField(max_length=100)
	producto = models.CharField(max_length=100)
	precio = models.CharField(max_length=20)
	impuesto = models.CharField(max_length=20)
	total = models.CharField(max_length=20)
	
