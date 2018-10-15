from django.db import models
from datetime import datetime

class Post(models.Model):
	title = models.CharField(max_length = 255)
	body = models.TextField()
	date = models.DateTimeField(default = datetime.now())


	def __str__(self):
		return self.title




class Comment(models.Model):
	comment= models.TextField()
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	date = models.DateTimeField(default = datetime.now())


	def __str__(self):
		return self.comment
	

# Create your models here.
