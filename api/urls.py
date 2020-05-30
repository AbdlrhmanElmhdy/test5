from django.urls import path
from .views import users_list, user_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('users/', users_list),
  path('users/<int:pk>/', user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)