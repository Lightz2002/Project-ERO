from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
	def create_user(self, company_name, city, address, email, password=None):
		if not company_name:
			raise ValueError('Company must have an company name')
		if not city:
			raise ValueError('Company must have an city')
		if not address:
			raise ValueError('Company must have an address')
		if not email:
			raise ValueError('Company must have an email address')

		user = self.model(
				company_name=company_name,
				city=city,
				address=address,
				email=self.normalize_email(email),
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,company_name,city,address,email,password):
		user = self.create_user(
				company_name=company_name,
				city=city,
				address=address,
				email=self.normalize_email(email),
			)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser =True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	company_name 	= models.CharField(verbose_name='company name', max_length=255,unique=True)
	city 			= models.CharField(max_length= 255)
	address			= models.CharField(max_length = 255)
	email 			= models.EmailField(max_length=255)
	date_joined 	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login	 	= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin	 	= models.BooleanField(default=False)
	is_active	 	= models.BooleanField(default=True)
	is_staff	 	= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)

	USERNAME_FIELD = 'company_name'
	REQUIRED_FIELDS = ['city', 'address', 'email']

	objects = MyAccountManager()

	def __str__(self):
		return self.company_name 

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True