# from rest_framework import status
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer

# # Create your views here.

# class UsersList(APIView):
#	 """
#	 List all code Users, or create a new User.
#	 """
#	 def get(self, request, format=None):
#	 users = User.objects.all()
#	 serializer = UserSerializer(users, many=True)
#	 return Response(serializer.data)

#	 def post(self, request, format=None):
#	 data = JSONParser().parse(request)
#	 serializer = UserSerializer(data=data)
#	 if serializer.is_valid():
#		 serializer.save()
#		 return Response(serializer.data, status=status.HTTP_201_CREATED)
#	 return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserDetail(APIView):
#	 """
#	 Retrieve, update or delete a user.
#	 """
#	 def get_object(self, pk):
#		 try:
#		 return User.objects.get(pk=pk)
#		 except User.DoesNotExist:
#		 raise Http404

#	 def get(self, request, pk, format=None):
#		 User = self.get_object(pk)
#		 serializer = UserSerializer(user)
#		 return Response(serializer.data)

#	 def put(self, request, pk, format=None):
#		 data = JSONParser().parse(request)
#		 serializer = UserSerializer(user, data=data)
#		 if serializer.is_valid():
#		 serializer.save()
#		 return Response(serializer.data)
#		 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#	 def delete(self, request, pk, format=None):
#		 user.delete()
#		 return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def users_list(request):
	"""
	List all code users, or create a new user.
	"""
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
	"""
	Retrieve, update or delete a code user.
	"""
	try:
		user = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
