import jwt
# import jwt.exceptions
import uuid
import warnings
from datetime import datetime, timedelta
from rest_framework_jwt.settings import api_settings
from django.db import transaction
from ..models import SysUser
# import traceback
from django.contrib.auth import authenticate
from ..library.exceptions import CustomAPIException
from rest_framework import status
from rest_framework.exceptions import NotFound

class AuthService(object):
    @staticmethod
    def generate_token(username, password):

        user_obj = ''
        try:
            # user_obj = SysUser.objects.get(username=username, password=password)
            user_obj = authenticate(username=username, password=password)
        except SysUser.DoesNotExist:
            raise NotFound()            
        # except:
        #     print(traceback.print_exc())     
        
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)

        return token

    @staticmethod
    def decode_token(token):
        jwt_encode_handler = api_settings.JWT_DECODE_HANDLER        
        payload = jwt_encode_handler(token)
        return payload  

    @staticmethod
    def init_data():
        try:
            with transaction.atomic():
                AuthService.clear_data()
                
                SysUser.objects.create_user(
                    username="user", 
                    email="user@com.tw", 
                    password="pwd", 
                    first_name="a",
                    last_name="b",
                    role="dev"
                )
                                    
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e)) 
        else:
            print("sys_user init success!")

    @staticmethod
    def clear_data():
        try:
            with transaction.atomic():
                susers = SysUser.objects.all()
                for suser in susers:
                    # suser.projs.clear()
                    suser.delete()      
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e))
        else:
            print("sys_user clear success!")          