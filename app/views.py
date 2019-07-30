from .cust_views import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import APIException
from .library.exceptions import CustomAPIException
# Create your views here.

@api_view() # def ['GET']
def index(request):
    return Response("Django DRF")

@api_view()
def error(request):

    # 模擬無法管控的例外
    raise Exception("test error!")

    # 模擬可管控的例外
    exc = CustomAPIException(        
        code="msg",
        detail="test error!",
        status_code=status.HTTP_501_NOT_IMPLEMENTED
        )    

    exc.add("state", "1111")

    print(exc.detail)
    print(exc.get_codes())
    print(exc.get_full_details())

    raise exc   

    # raise CustomAPIException(
    #     detail="test error!",
    #     code="error",
    #     status_code=status.HTTP_501_NOT_IMPLEMENTED) 

    return Response("Hello World")        
           