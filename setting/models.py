from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Uom(models.Model):
	uom = models.CharField(max_length=20)		
	quantity = models.IntegerField()

	def __str__(self):
		return self.uom + ' (' + str(self.quantity) + ')'

	class Meta(object):
		db_table = "Uom"


class Warehouse(models.Model):
	warehouse_name = models.CharField(max_length=100)		
	location = models.CharField(max_length=255)


	def __str__(self):
		return self.warehouse_name 

	class Meta(object):
		db_table = "Warehouse"


class Supplier(models.Model):
	supplier_name = models.CharField(max_length=100)		
	telephone_number = PhoneNumberField(blank=True)
	email = models.EmailField(max_length=255)
	location = models.CharField(max_length=255)

	def __str__(self):
		return self.supplier_name 

	class Meta(object):
		db_table = "Supplier"

class Category(models.Model):
	category = models.CharField(max_length=100)		

	def __str__(self):
		return self.category 

	class Meta(object):
		db_table = "Category"
