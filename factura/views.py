from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class Facturaview(View):
	"""docstring for Class"""
	def get(self, request):
		return HttpResponse("Hola 1")

		