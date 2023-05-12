from django.urls import path
from .views import GenerateTokenView
from .views import UserCreateView
from .views import UserListView

urlpatterns = [
    path('generate-token/', GenerateTokenView.as_view(), name='generate_token'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('users/list/', UserListView.as_view(), name='user-list'),
  
]