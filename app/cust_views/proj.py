from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from ..cust_models.proj import *

class ProjAPIView(APIView):
    
    def get(self, request, id, format=None):
        try:
            item = Proj.objects.get(pk=id)
            serializer = ProjSerializer(item)
            return Response(serializer.data)
        except Proj.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Proj.objects.get(pk=id)
        except Proj.DoesNotExist:
            return Response(status=404)
        serializer = Proj(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Proj.objects.get(pk=id)
        except Proj.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

class ProjListAPIView(APIView):

    http_method_names = ['get', 'post']
    
    def get(self, request, format=None):
        items = Proj.objects.all()
        serializer = ProjSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)        
