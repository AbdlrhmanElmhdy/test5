from .models import User
from .serializers import UserSerializer
from rest_framework import generics

# Create your views here.

class UsersList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer