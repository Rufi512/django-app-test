import re
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import CustomerSerializer, MyTokenObtainPairSerializer
from .models import Customer
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAuthenticated
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework_simplejwt.views import TokenObtainPairView




# Create your views here.

class Customer(viewsets.ModelViewSet):
	queryset = Customer.objects.all().order_by('-date_joined')
	serializer_class = CustomerSerializer
	lookup_field = 'customer'

	def get_permissions(self):
		if self.action in ['list','update', 'partial_update', 'destroy']:
			self.permission_classes = [IsAuthenticated,]
		elif self.action in ['create']:
			self.permission_classes = [permissions.AllowAny,]
		return super().get_permissions()

def login_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		return redirect('home')
		print(request.user.is_authenticated)
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user_login = authenticate(request, email = email, password = password)
		if user_login is not None:
			login(request, user_login)
			return redirect('home')
		else:
			return redirect('login')
			#redirect('login')

	context={
	"type":"login"
	}
	return render(request, "login.html",context)

def register_view(request, *args, **kwargs):
	context={
	"type":"register"
	}
	return render(request, "login.html",context)

def logout_view(request):
	logout(request)
	return redirect('home')

class MyTokenObtainPairView(TokenObtainPairView):
	def get_serializer_class(self):
		return MyTokenObtainPairSerializer
		#return MyTokenObtainPairSerializer
    #serializer_class = MyTokenObtainPairSerializer