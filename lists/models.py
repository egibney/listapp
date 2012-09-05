from django.db import models

class List(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return "List: " + self.name



class Item(models.Model):
	name = models.CharField(max_length=200)
	list = models.ForeignKey(List)
	url = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return "Item: " + self.name



