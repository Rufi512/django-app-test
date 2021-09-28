from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.

#Render API
class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	def get_queryset(self):
		products = Product.objects.all()
		return products

	def destroy(self, request, *args, **kwargs):
		product = self.get_object()
		self.get_object().image.delete()
		self.get_object().delete()
		return Response("Product Delete")
		
#Render views
def home_view(request,*args, **kwargs):
	context ={
	"products": Product.objects.all()
	}
	return render(request,"home.html",context)

def contact_view(request,*args, **kwargs):
	context={
	"number_phone": "+1-(999)-999-9999",
	"name":"Rufi512"
	}
	return render(request,"contact.html",context)

def upload_view(request,*args, **kwargs):
	if request.method == "POST":
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ProductForm()
		print(request)
	context = {
	'form':form
	}
	return render(request,"upload.html",context)

def modify_view(request,product_id,*args, **kwargs):
	product_modify = Product.objects.get(pk=product_id)
	if request.method == "POST":
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			product_modify.title = request.POST.get('title')
			product_modify.price = request.POST.get('price')
			product_modify.description = request.POST.get('description')
			if request.FILES:
				product_modify.image.delete()
				product_modify.image = request.FILES.get('image')
			if request.POST.get('avalaible'):
				product_modify.avalaible = True
			else:
				product_modify.avalaible = False
			product_modify.save()
			return redirect('home')
	else:
		print(request)
		form = ProductForm()
	context = {
	'form':form,
	'type':'modify',
	'product_modify':product_modify
	}
	return render(request,"upload.html",context)


	
