from django.urls import path
# from .views import users_list, user_detail
from .views import UsersList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('users/', UsersList.as_view()),
  path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)