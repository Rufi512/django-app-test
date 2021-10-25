from .models import Customer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Customer
		fields = ('id','username', 'email', 'password', 'is_staff')

	def create(self, validated_data):
		user = Customer.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			)
		user.set_password(validated_data['password'])
		user.save()
		return user

class CustomerProductSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Customer
		fields = ('username','is_staff')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
    	token = super().get_token(user)
    	return token
"""
	def validate_username(self,data):
		customers = Customer.objects.filter(username = data)
		if len(customers) != 0:
			raise serializers.ValidationError("It's username exists, try with other one")
		else:
			return data
"""