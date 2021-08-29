from slime_behavior.models import Slime, SlimeTypes, Action
from random import choice

if __name__ == '__main__':
	types = ['anemo', 'dendro', 'cryo', 'geo', 'hydro', 'pyro', 'electro']
	slime_types = SlimeTypes.objects.all().values_list('description', flat=True)
	for i,type in enumerate(types):
		if type not in slime_types:
			SlimeTypes.objects.create(description=type, type_index=len(slime_types) + i)


	actions = ['jump', 'sleep', 'sing', 'drink', 'run', 'read', 'smile', 'stay', 'arrr!', 'dance']
	for action in actions:
		Action.objects.get_or_create(action_name=action)



	slimes = ['Do-do', 'Arrr', 'Nata', 'Sleepy', 'Urr-Urr', 'Urr', 'Nunu', 'Vilgelm']
	for slime in slimes:
		action = choice(actions)
		type = choice(types)
		Action.objects.get_or_create(name=slime, defaults={'type': SlimeTypes.objects.get(description=type), 
														   'action': Action.objects.get(action_name=action)})