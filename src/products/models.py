from django.db import models		# models is  basically how u connect the django to the database
import os
import random
from .utils import unique_slug_generator 
from django.db.models.signals import pre_save
# Create your models here.

def get_file_name(filepath):
	base_name = os.path.basename(filepath) #
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance,filename):
	new_filename= random.randint(1,20)
	name, ext	= get_file_name(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

class Product(models.Model):
	title		= models.CharField(max_length=120)
	slug		= models.SlugField(blank=True)
	description	= models.TextField()
	price		= models.DecimalField(decimal_places=2,max_digits=10, default= 39.99)
	image		= models.ImageField(upload_to= upload_image_path, null=True, blank=True)				# it uploads to media Root, null= true means its not necessry to provide the field and blank true means django wont cos any problem even if u dont provide it stuff
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/products/{slug}/".format(slug= self.slug)

def product_pre_save_receiver(sender, instance,*args,**kwargs):
	if not instance.slug:
		instance.slug= unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender= Product)