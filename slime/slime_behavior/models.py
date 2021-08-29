from django.db import models
from datetime import datetime


class Action(models.Model):
	action_name = models.CharField(max_length=70)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.action_name


class SlimeTypes(models.Model):
	type_index = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=50)

	def __str__(self):
		return self.description


class Slime(models.Model):
	action = models.ForeignKey("Action", on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	type = models.ForeignKey("SlimeTypes", on_delete=models.CASCADE, to_field='type_index')

	
	color = models.TextField(default='No color')

	def set_color(self):
		if self.type.description == 'pyro':
			self.color = 'orange'
		elif self.type.description == 'hydro':
			self.color = 'blue'
		else:
			self.color = 'green'
		self.save()
	
	def __str__(self):
		return self.name

	def change_action(self, new_action):
		if self.action.action_name != new_action:
			action, _ = Action.objects.get_or_create(action_name=new_action, defaults={'pub_date': datetime.now()})
			self.action = action
			self.save()
			print('Ok lets do this >_<')
		else:
			print('I am doing it!! -_-')

