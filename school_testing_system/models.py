from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Tasks(models.Model):
	"""zada4ka
	"""
	name = models.CharField(max_length = 100)
	text = models.TextField()
	task_path_input = models.CharField(max_length = 300)
	task_path_output = models.CharField(max_length = 300)

	def __str__(self):
		return self.task

class Solution(models.Model):
	"""
	reshenie
	"""
	task = models.ForeignKey(
		'Tasks',
		on_delete=models.CASCADE,
		)
	source = models.FileField(upload_to='upload')
