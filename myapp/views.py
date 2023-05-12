# Create your views here.
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from oauthlib.common import generate_token
from django.db.models import Q
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser

class GenerateTokenView(APIView):
    def post(self, request):
        access_token = generate_token()
        expires_in = datetime.now() + timedelta(minutes=3)
        data = {
            'access_token': access_token,
            'expires_in': expires_in,
        }
        return Response(data, status=status.HTTP_200_OK)



class UserCreateView(APIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_scope = 'user'

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    permission_classes = [IsAdminUser]
    throttle_scope = 'user'
    throttle_scope = 'anon'

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        user_list = User.objects.all().order_by('-created_date')
        result_page = paginator.paginate_queryset(user_list, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
