from django.db import models

class Task_list(models.Model):
	name = models.CharField(max_length = 255)
	
	def __str__(self):
		return self.name


class Task(models.Model):
	task_name = models.CharField(max_length = 255)
	created = models.DateTimeField(auto_now_add = True)
	due_on = models.DateTimeField()
	owner = models.CharField( max_length = 255, default= "Admin")
	mark = models.BooleanField( default = False)
	task_list = models.ForeignKey(Task_list, on_delete=models.CASCADE, default = None)

	def __str__(self):
		return self.task_name