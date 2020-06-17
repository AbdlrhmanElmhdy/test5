# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from .serializers import UserSerializer
# from rest_framework import generics
# from rest_framework import permissions

# # Create your views here.

# class UsersList(generics.ListCreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Customer

class AuthVerification(APIView):
	# authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		content = {
			'user': str(request.user),  # `django.contrib.auth.User` instance.
			'auth': str(request.auth),  # None
		}
		return Response(content)

class CreateUser(APIView):
	def post(self, request):
		username = request.data.get('username')
		email = request.data.get('email')
		password = request.data.get('password')
		first_name = request.data.get('firstName')
		last_name = request.data.get('lastName')
		phone_number = request.data.get('phone_number')
		user_type = request.data.get('userType')

		user = User.objects.create_user(
			username=username,
			email=email,
			password=password,
			first_name=first_name,
			last_name=last_name
		)

		if user_type == 'CUSTOMER':
			customer = Customer(user=user, phone_number=phone_number)
			customer.save()

		token = Token.objects.create(user=user)

		return Response(token.key, status=status.HTTP_201_CREATED)

class CustomersList(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		user = request.user
		customers = Customer.objects.all()
		serializer = CustomerSerializer(customers, many=True)
		return Response(serializer.data)

class UsersList(APIView):
	def get(self, request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)