from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product, Categories
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import ProductSerializer, CategoriesSerializer

# Create your views here.

#Render API

class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	
	def get_permissions(self):
		if self.action in ['create','update', 'partial_update', 'destroy']:
			self.permission_classes = [IsAuthenticated,]
		elif self.action in ['list']:
			self.permission_classes = [permissions.AllowAny,]
		return super().get_permissions()

	def get_queryset(self):
		products = Product.objects.all()
		return products

	def create(self,request):
		avalaible_product = lambda x: True if x == "true" != None else False
		product = Product.objects.create(
			title = request.POST.get('title'),
			description = request.POST.get('description'),
			price = request.POST.get('price'),
			avalaible = avalaible_product(request.POST.get('avalaible')) ,
			seller = request.user,
			image = request.FILES.get('image')
			)
		product.save()
		return Response(data={'message':'Product Created!'})
				
	

	def update(self, request, pk):
		avalaible_product = lambda x: True if x == "true" != None else False
		product = self.get_object()
		image_product = product.image
		if request.user != product.seller and request.user.is_staff == False:
			return Response(data={'message':'You no have permissions to modify this product!'},status=status.HTTP_400_BAD_REQUEST)
		if request.POST.get("delete_image") == "true" or request.FILES.get('image'):
			try:
				self.get_object().image.delete()
			except:
				pass
			if request.FILES.get('image'):
				image_product = request.FILES.get('image')
			else:
				image_product = None

		product_modify = {
		'title': request.POST.get('title'),
			'description': request.POST.get('description'),
			'price': request.POST.get('price'),
			'avalaible': avalaible_product(request.POST.get('avalaible')),
			'image': image_product
		}

		serializer = ProductSerializer(product, data=product_modify)
		if serializer.is_valid():
			serializer.save()
			return Response(data={'message':'Product Modify!'})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
	def destroy(self, request, *args, **kwargs):
		product = self.get_object()
		if request.user != product.seller and request.user.is_staff == False:
			return Response(data={'message':'You no have permissions to delete this product!'},status=status.HTTP_400_BAD_REQUEST)
		try:
			self.get_object().image.delete()
		except:
			pass
		self.get_object().delete()
		return Response("Product Delete")


#Render productView

class CategoriesViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	def get_queryset(self):
		categories = Categories.objects.all()
		return categories

#Render views


def home_view(request,*args, **kwargs):
	context ={
	"user":request.user,
	"products": Product.objects.all(),
	"categories": Categories.objects.all()
	}
	return render(request,"home.html",context)

def contact_view(request,*args, **kwargs):
	context={
	"user":request.user,
	"number_phone": "+1-(999)-999-9999",
	"name":"Rufi512"
	}
	return render(request,"contact.html",context)

def upload_view(request,*args, **kwargs):
	if not request.user.is_authenticated:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	if request.method == "POST":
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ProductForm()
	context = {
	"user":request.user,
	'form':form
	}
	return render(request,"upload.html",context)

def modify_view(request,product_id,*args, **kwargs):
	product_modify = Product.objects.get(pk=product_id)
	if not request.user.is_authenticated:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	if request.user.username != product_modify.seller.username and request.user.is_staff == False:
		return redirect('home')
	form = ProductForm()
	context = {
	"user":request.user,
	'form':form,
	'product_modify': product_modify,
	'type':'modify'
	}
	return render(request,"upload.html",context)


def product_view(request,*args, **kwargs):
	return render(request,"product.html",{})

def cart_view(request,*args, **kwargs):
	return render(request,"cart_items.html",{})

def checkout_view(request,*args, **kwargs):
	return render(request,"checkout.html",{})


	
