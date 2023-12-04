from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model=Blog
		fields=('blog_id','blog_title','blog_contact','blog_created','blog_updated')