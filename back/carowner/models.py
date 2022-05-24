from django.db import models
from parkingowner.models import Parking
from users.models import CustomUser
from datetime import datetime, timedelta

# Create your models here.


#Car Owner Model

class CarOwner(models.Model):
	user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	favoriteLocations = models.CharField(max_length=100,blank=True)
	cash = models.IntegerField(default=0,blank=True)

	def __str__(self):
		return self.user.email



# Car Model

class Car(models.Model):
	owner = models.ForeignKey(CarOwner,on_delete=models.CASCADE)
	carName = models.CharField(max_length=100)
	pelak = models.CharField(max_length=8,unique=True)
	color = models.CharField(max_length=100)
	

	def __str__(self):
		return self.pelak


#Comment Model

class Comment(models.Model):
	parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	content = models.TextField()
	dateAdded = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

	
	@property
	def children(self):
		return Comment.objects.filter(parent=self).all()

	@property
	def is_parent(self):
		if self.parent is None:
			return True
		return False

	def __str__(self):
		return self.content


#Rating Model

class Rate(models.Model):
	parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
	owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
	value = models.PositiveIntegerField(default=0)



#Reservation Model

class Reservation(models.Model):
	owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
	parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	trackingCode = models.IntegerField(default=0)
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	cost = models.FloatField(default=0)
