from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

class UploadsAPIView(APIView):
    
    def post(self, request, format=None):

        filenames = [f.name for f in request.FILES.getlist('files')]

        return Response(filenames, status=200)

class UploadAPIView(APIView):
    
    def post(self, request, format=None):

        f = request.FILES.get('file', None)

        filename = f.name

        return Response(filename, status=200)        

class Upload2APIView(APIView):
    
    def post(self, request, format=None):

        f1 = request.FILES.get('file1', None)
        f2 = request.FILES.get('file2', None)
        filenames = [f1.name, f2.name]

        return Response(filenames, status=200)          