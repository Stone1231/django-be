from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from ..cust_services import auth
import json

class LoginAPIView(APIView):

    permission_classes = (permissions.AllowAny,)

    def put(self, request, format=None):
        body_data = request.body.decode('utf-8')
        request_data = json.loads(body_data)

        username = request_data["username"]
        password = request_data["pwd"]

        token = auth.AuthService.generate_token(username, password)
            
        return Response({
            'token': token
            },
            status=status.HTTP_200_OK)


class AuthAPIView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, format=None):
        # payload = auth.AuthService.generate_token()
        return Response({
            'username': self.request.user.username,
            'role': self.request.user.role
            },
            status=status.HTTP_200_OK)
        # return Response(self.request, status=status.HTTP_200_OK)

class AnonymousAPIView(APIView):

    permission_classes=(permissions.AllowAny,)

    def get(self, request, format=None):
        return Response("For all anonymous.", status=status.HTTP_200_OK)
