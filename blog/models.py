from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 30,verbose_name='Username')
	headImg = models.FileField(upload_to = './upload/')
	def __unicode__ (self):
		return self.name,self.headImg

class Book(models.Model):
	Book_name = models.CharField(max_length=100)
	Book_author= models.CharField(max_length=100)
	Book_price = models.IntegerField()
	Book_publisher =models.CharField(max_length=100)
	Book_status = models.CharField(max_length=100)
	release_date = models.DateField()
	
	def __unicode__ (self):
		return self.Book_name
		