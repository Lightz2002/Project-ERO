from django.db import models
from login.models import Account 
from product.models import Product
from setting.models import *
# from product.models 
# Create your models here.
class Retur(models.Model):
	document_name = models.CharField(max_length=100,unique=True)
	date = models.DateField(auto_now=False,editable=True)
	warehouse_name = models.ForeignKey(Warehouse,null=True,on_delete=models.SET_NULL)
	supplier_name = models.ForeignKey(Supplier,null=True,on_delete=models.SET_NULL)
	product_name = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
	quantity = models.IntegerField()
	uom = models.ForeignKey(Uom,null=True,on_delete=models.CASCADE)
	product_price = models.IntegerField()

	@property
	def total(self):
		return self.quantity * self.uom.quantity * self.product_price
	
	def __str__(self):
		return self.document_name

	class Meta(object):
		db_table = "retur"
			
