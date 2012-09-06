from lists.models import List, Item
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	lists = List.objects.all().order_by('-pub_date')[:5]
	context = {"lists": lists}
	return render_to_response(
		'index.html',
		context,
		context_instance=RequestContext(request)
	)

def detail(request, id):
	list = List.objects.get(id=id)
	context = {"list": list}	
	# list_items = Item.objects.filter(list_id=id)
	# list_items = Item.objects.filter(list=list)
	return render_to_response(
		'detail.html',
		context,
		context_instance=RequestContext(request)
	)

def create_list(request):
	context = {"list": list}	
	return render_to_response(
		'create_list.html',
		context,
		context_instance=RequestContext(request)
	)