from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username']

class CustomerSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=True)

	class Meta:
		model = Customer
		fields = ['user', 'phone_number']