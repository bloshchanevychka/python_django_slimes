from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import loader
from django.urls import reverse
from .models import Slime, Action, SlimeTypes
from django.views import generic
from django.db.models import Q

class IndexView(generic.ListView):
    template_name = 'slime_behavior/index.html'
    context_object_name = 'all_slimes'

    def get_queryset(self):
        """Return all slimes."""
        return Slime.objects.filter(~Q(color='No color')).order_by('-name')[:]


class DetailsView(generic.DetailView):
	model = Slime
	template_name = 'slime_behavior/details.html'

	def get_queryset(self):
		"""Return all slimes."""
		return Slime.objects.filter(~Q(color='No color'))


def slime_action(request, slime_name):
	slime = get_object_or_404(Slime, name=slime_name)
	try:
		selected_action = Action.objects.get(id=request.POST['action_id'])

	except (KeyError, Action.DoesNotExist):
		return render(request,'slime_behavior/slime.html', {'slime': slime,
															'all_actions':Action.objects.order_by('-action_name')[:] , 
										'error_message': f"Select something, stupid human!! *@%$& {request.POST}"})
	else:
		if slime.action.action_name == selected_action.action_name:
			return render(request,'slime_behavior/action_change.html',{'slime': slime, 
															'all_actions': Action.objects.order_by('-action_name')[:]})
		else:
			return HttpResponseRedirect(reverse('slime_behavior:index'))
			#HttpResponse('Nope, stupid human!!><')


def action_change(request, slime_name):
	slime = get_object_or_404(Slime, name=slime_name)
	try:
		slime.action = Action.objects.get(id=request.POST['action_id'])
		slime.save()

	except (KeyError, Action.DoesNotExist):
		return render(request,'slime_behavior/action_change.html', {'slime': slime,
															'all_actions':Action.objects.order_by('-action_name')[:] , 
										'error_message': f"Select something, stupid human!! *@%$& {request.POST}"})
	else:
		return render(request,'slime_behavior/action_changed.html')


def slime(request, slime_name):
	try:
		slime = Slime.objects.get(name=slime_name)
		all_actions = Action.objects.order_by('-action_name')[:]
		return render(request, 'slime_behavior/slime.html', {'slime': slime, 'all_actions': all_actions})
	except Slime.DoesNotExist:
		raise Http404(f'Slime {slime_name} is drunk as fuck. Try to call later')



##TODO: Use the template system
def slime_by_id(request, slime_id):
#	#slime_type = 'pyro'
	#slime = Slime.objects.get(id=2)
	slime_type = Slime.objects.get(id=slime_id).type
	slime_name = Slime.objects.get(id=slime_id).name
	return HttpResponse(f'My name is {slime_name}. I am a {slime_type} slime!')
	#return HttpResponse(slime)


# Create your views here.
