from django.db import transaction
from ..cust_models.dept import *
from ..library.exceptions import CustomAPIException
from rest_framework import status

class DeptService(object):
    @staticmethod
    def init_data():
        names = ["dept1", "dept2", "dept3"]
        try:
            with transaction.atomic():
                DeptService.clear_data()
                i = 1
                for n in names:                    
                    item: Dept = Dept()
                    item.id = i
                    item.name = n
                    item.save()
                    i = i + 1
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e))             
        else:
            print("dept init success!")

    @staticmethod
    def clear_data():
        try:
            with transaction.atomic():
                Dept.objects.all().delete()     
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e))            
        else:
            print("dept clear success!")              