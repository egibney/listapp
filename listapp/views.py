from lists.models import List, Item
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
	context="asdf"
	return render_to_response(
		'home.html',
		context,
		context_instance=RequestContext(request)

	)

def registration_form(request):
	context="asdf"
	return render_to_response(
		'registration_form.html',
		context,
		context_instance=RequestContext(request)

	)