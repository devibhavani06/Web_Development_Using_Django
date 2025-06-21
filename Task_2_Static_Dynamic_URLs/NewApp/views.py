from django.shortcuts import render
from django.http import HttpResponse

# Static url.
def static_url(request):
	return HttpResponse("<h1 style=color:navy;text-align:center>This is Static URL</h1>")

#Dynamic url
def dynamic_url(request,name,id):
	return HttpResponse("<h1 style=text-align:center><i>My name is {} and my id is {}</h1></i>".format(name,id))
