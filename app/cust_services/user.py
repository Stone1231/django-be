from django.db import transaction
from ..cust_models.user import *
from datetime import datetime
from ..library.exceptions import CustomAPIException
from rest_framework import status

class UserService(object):
    @staticmethod
    def init_data():
        try:
            with transaction.atomic():
                UserService.clear_data()

                item = User()
                item.name="user1"
                item.hight = 170
                item.photo = ""
                item.birthday = datetime(1977, 12, 31, 12, 0, 0)
                item.dept = Dept.objects.get(id=1)
                item.save()
                                
                projs = Proj.objects.all()
                for proj in projs:
                    mapping = UserProjMapping()
                    mapping.user = item
                    mapping.proj = proj
                    mapping.save()
                                    
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e))            
        else:
            print("user init success!")

    @staticmethod
    def clear_data():
        try:
            with transaction.atomic():
                users = User.objects.all()
                for user in users:
                    user.projs.clear()
                    user.delete()
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e))            
        else:
            print("user clear success!")      