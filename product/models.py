from django.db import models
from setting.models import *
# Create your models here.

class Product(models.Model):	
	product_name = models.CharField(max_length=100)
	photo = models.ImageField(null=True,blank=True)
	purchase_price = models.IntegerField()
	selling_price = models.IntegerField()
	supplier_name = models.ForeignKey(Supplier,blank=True,null=True,on_delete=models.SET_NULL)
	barcode = models.IntegerField()
	uom = models.ForeignKey(Uom,null=True,blank=True,on_delete=models.SET_NULL)
	category = models.ForeignKey(Category,blank=True,null=True,on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.product_name 

	@property
	def photo_url(self):
		if self.photo and hasattr(self.photo, 'url'):
			return self.photo.url
		else:
			return "logo.png"


	class Meta(object):
		db_table = "Product"

