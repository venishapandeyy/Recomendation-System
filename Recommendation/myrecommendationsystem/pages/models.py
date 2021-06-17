from django.db import models
from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Moviess(models.Model):
	name = models.CharField(default="Movie Name",max_length=100)
	descriptions = models.TextField(null=False,default="This is the amazing movie.",max_length=500)
	image = models.ImageField(upload_to='images/',blank=False)
	genre = models.CharField(max_length=100, default='')
	video = models.FileField(upload_to='', null=True,blank=True)

	def __str__(self):
		return self.name
		return self.descriptions

class Myrating(models.Model):
	user   	= models.ForeignKey(User,on_delete=models.CASCADE)
	Movies 	= models.ForeignKey(Moviess,on_delete=models.CASCADE, default=None)
	rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])



# Create your models here.

class Contactus(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    emails = models.EmailField(max_length=200,null=True,blank=True)
    subjects = models.CharField(max_length=100,null=True,blank=True)
    descriptions = models.CharField(max_length=400,null=True,blank=True)

