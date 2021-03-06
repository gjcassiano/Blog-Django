from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comentario(models.Model):
	 nome = models.CharField(max_length=50)
	 email = models.CharField(max_length=100)
	 site = models.CharField(max_length=100)
	 texto = models.TextField(max_length=255)

class Post(models.Model):
	post_id = models.AutoField(primary_key=True)	
	title = models.CharField(max_length = 100)
	texto = models.TextField()
	date = models.DateField()
