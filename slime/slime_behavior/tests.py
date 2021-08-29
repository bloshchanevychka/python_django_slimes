from django.test import TestCase
from .models import Slime, Action, SlimeTypes
from django.urls import reverse
# Create your tests here.


class SlimeModelTest(TestCase):

	def setUp(self):
		self.slime_dendro = Slime.objects.create(
			name='Sleepy', 
			action=Action.objects.create(action_name='sleep'),
			type=SlimeTypes.objects.create(type_index=1, description='dendro')
		)

		self.slime_pyro = Slime.objects.create(
			name='Fire', 
			action=Action.objects.create(action_name='sleep'),
			type=SlimeTypes.objects.create(type_index=2, description='pyro')
		)

		self.slime_hydro = Slime.objects.create(
			name='Bubles', 
			action=Action.objects.create(action_name='sleep'),
			type=SlimeTypes.objects.create(type_index=3, description='hydro')
		)

	def test_set_slime_color_default(self):

		color = 'No color'
		#self.slime_dendro.set_color()
		#rint(self.slime_dendro.color is color)
		self.assertEqual(self.slime_dendro.color, color)

	def test_set_slime_color_other(self):
		
		color = 'orange'
		self.slime_pyro.set_color()
		self.assertEqual(self.slime_pyro.color, color)


class SlimeIndexViewTest(TestCase):

	def create_slime(self):
		self.slime_dendro = Slime.objects.create(
			name='Sleepy', 
			action=Action.objects.create(action_name='sleep'),
			type=SlimeTypes.objects.create(type_index=1, description='dendro')
		)

		self.slime_pyro = Slime.objects.create(
			name='Fire', 
			action=Action.objects.create(action_name='sleep'),
			type=SlimeTypes.objects.create(type_index=2, description='pyro')
		)

		self.slime_hydro = Slime.objects.create(
			name='Bubles', 
			action=Action.objects.create(action_name='sleep'),
			type=SlimeTypes.objects.create(type_index=3, description='hydro')
		)

	def test_no_slimes(self):

		response = self.client.get(reverse('slime_behavior:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No slimes are available.")
		self.assertQuerysetEqual(response.context['all_slimes'], [])

	def test_add_color_one_slime(self):

		self.create_slime()
		self.slime_pyro.set_color()
		response = self.client.get(reverse('slime_behavior:index'))
		self.assertQuerysetEqual( response.context['all_slimes'],['<Slime: Fire>'])

	def test_no_color_slimes(self):

		self.create_slime()
		response = self.client.get(reverse('slime_behavior:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No slimes are available.")
		self.assertQuerysetEqual(response.context['all_slimes'], [])

	def test_future_question_and_past_question(self):
		self.create_slime()
		self.slime_dendro.set_color()
		response = self.client.get(reverse('slime_behavior:index'))
		self.assertQuerysetEqual(response.context['all_slimes'],['<Slime: Sleepy>'])

	def test_two_past_questions(self):
		self.create_slime()
		self.slime_hydro.set_color()
		self.slime_pyro.set_color()
		response = self.client.get(reverse('slime_behavior:index'))
		self.assertQuerysetEqual(response.context['all_slimes'],['<Slime: Fire>', '<Slime: Bubles>'])
	

class SlimeDetailViewTests(TestCase):
	def setUp(self):
		self.slime_dendro = Slime.objects.create(
				name='Sleepy', 
				action=Action.objects.create(action_name='sleep'),
				type=SlimeTypes.objects.create(type_index=1, description='dendro')
		)

		self.slime_pyro = Slime.objects.create(
				name='Fire', 
				action=Action.objects.create(action_name='sleep'),
				type=SlimeTypes.objects.create(type_index=2, description='pyro')
		)
		self.slime_pyro.set_color()

		self.slime_hydro = Slime.objects.create(
				name='Bubles', 
				action=Action.objects.create(action_name='sleep'),
				type=SlimeTypes.objects.create(type_index=3, description='hydro')
		)

	def test_no_color_slime(self):
			
		url = reverse('slime_behavior:slime_details', args=(self.slime_dendro.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code,404)

	def test_colorfull_slime(self):

		url = reverse('slime_behavior:slime_details', args=(self.slime_pyro.id,))
		response = self.client.get(url)
		self.assertContains(response, self.slime_pyro.color)