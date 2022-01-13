from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
	title=(models.CharField(max_length=10))
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now) #auto_now=True used for getting the current data  auto_now_add used when the post was posted
 
	author=models.ForeignKey(User,on_delete=models.CASCADE) #Foreign Key as User Post more than one post so one to many rel.


	def __str__(self):
		return "Title: "+self.title+"\n"+"Content: "+self.content+"\n"+"Date_posted: "+str(self.date_posted)+"\n"+"Author: "+str(self.author) +"\n"










