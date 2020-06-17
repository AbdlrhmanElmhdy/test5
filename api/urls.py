from django.urls import path
from .views import AuthVerification, CreateUser, CustomersList, UsersList
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('AuthVerification/', AuthVerification.as_view()),
  path('CreateUser/', CreateUser.as_view()),
  path('api-token-auth/', obtain_auth_token),
  path('customers/', CustomersList.as_view()),
  path('users/', UsersList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)