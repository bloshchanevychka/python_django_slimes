from django.urls import path

from . import views

app_name = 'slime_behavior'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<str:slime_name>/action', views.slime_action, name='action'),
	path('details/<int:pk>', views.DetailsView.as_view(), name='slime_details'),
	path('<str:slime_name>/action_change', views.action_change, name='action_change'),
	path('<str:slime_name>', views.slime, name='slime'),
]