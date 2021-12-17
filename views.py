from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Libreria

def index(request):
	return HttpResponse("Hola Mundo. Nombre de App")

class IndexView(generic.ListView):
	template_name = 'apptp/index.html'
	context_object_name = 'libreria_list'

	def get_queryset(self):
		return Libreria.objects.order_by('-id')