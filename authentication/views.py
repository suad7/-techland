from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializer import UserLoginSerializer,RegistrationSerializer
from rest_framework.permissions import AllowAny




@api_view(['POST',])
def register_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully created new user'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)






class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class= UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer= UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.erros, status=HTTP_400_BAD_REQUEST)

    