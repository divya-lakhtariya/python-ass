from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_id=models.PositiveIntegerField(blank=True)
	blog_title=models.CharField(max_length=100,blank=True)
	blog_contact=models.CharField(max_length=100,blank=True)
	blog_created=models.PositiveIntegerField(blank=True)
	blog_updated=models.PositiveIntegerField(blank=True)


	def __str__(self):
		return self.title
