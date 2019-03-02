from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 5:
			errors["name"] = "Name must be at least 5 characters long"
		if len(postData['desc']) < 15:
			errors["desc"] = "Description must be at least 15 characters long"
		return errors
		
class courses(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = CourseManager()