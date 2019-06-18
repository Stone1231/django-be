# from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# from .. import cust_models
# from ..cust_models.user import *
# from ..cust_models import User, UserSerializer
from ..cust_models import *

# from ..cust_models.aa import *
# from ..cust_models.bb import *
# from ..cust_models.cc import *

class UserAPIView(APIView):
    
    def get(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
            serializer = UserSerializer(item)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = User(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

class UserListAPIView(APIView):

    # http_method_names = ['get', 'post']
    
    def get(self, request, format=None):
        items = User.objects.all()
        serializer = UserSimpleSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)        

# 分頁之後再研究
class UserPageListAPIView(APIView):
    
    def get(self, request, format=None):
        items = User.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserSimpleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
