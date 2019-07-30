import os
import datetime
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# from .. import cust_models
# from ..cust_models.user import *
# from ..cust_models import User, UserSerializer
from ..cust_models import *
from ..cust_services import FileService

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
        serializer = UserSerializer(item, data=request.data)
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


class UserImgAPIView(APIView):

    # http_method_names = ['get', 'post']

    def post(self, request, format=None):
        file_obj = request.FILES.get('file', None)

        # if not file_obj:
        #     return Response("File object is None.", status=400)

        # if file_obj.size > settings.ATT_SIZE_LIMIT:
        #     return Response(
        #         "Oops, the file is too large ({0})".format(file_obj.size),
        #         status=415)

        # dir_name = os.path.join(settings.FILE_PATH, 'img')

        # if not os.path.exists(dir_name):
        #     os.mkdir(dir_name)

        # sep_index = file_obj.name.rfind(os.sep)
        # file_origin_name = file_obj.name if sep_index < 0 else file_obj.name[
        #     sep_index + 1:]
        # ext_index = file_origin_name.rfind('.')
        # ext_name = file_origin_name[ext_index:].lower()

        # if ext_name not in settings.ATT_TYPES:
        #     return Response(
        #         "Oops, we do NOT support this type ({0})".format(ext_name),
        #         status=415)

        # file_name = "{0}_{1}{2}".format(
        #     file_origin_name[: ext_index],
        #     datetime.datetime.now().timestamp(),
        #     ext_name)
        # full_name = os.path.join(dir_name, file_name)

        # with open(full_name, 'wb+') as destination:
        #     for chunk in file_obj.chunks():
        #         destination.write(chunk)

        file_name = FileService.upload(file_obj,"img")
        return Response(file_name, status=200)

class UserQueryListAPIView(APIView):
    
    def post(self, request, format=None):
        name = request.data
        items = User.objects.filter(name__contains=name)
        serializer = UserSimpleSerializer(items, many=True)
        return Response(serializer.data)

# 分頁之後再研究
class UserPageListAPIView(APIView):

    def get(self, request, format=None):
        items = User.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = UserSimpleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
