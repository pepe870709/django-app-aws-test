from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from users.domain.services import get_all_users

@api_view(["GET"])
def list_users(request):
    users = get_all_users()
    data = UserSerializer(users, many=True).data
    return Response(data)
