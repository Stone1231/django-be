from django.db import transaction
from ..cust_models.proj import *
from ..library.exceptions import CustomAPIException
from rest_framework import status

class ProjService(object):
    @staticmethod
    def init_data():
        names = ["proj1", "proj2", "proj3"]
        try:
            with transaction.atomic():
                ProjService.clear_data()
                i = 1
                for n in names:                    
                    item: Proj = Proj()
                    item.id = i
                    item.name = n
                    item.save()
                    i = i + 1
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e))             
        else:
            print("proj init success!")

    @staticmethod
    def clear_data():
        try:
            with transaction.atomic():
                projs = Proj.objects.all()
                for proj in projs:
                    proj.users.clear()
                    proj.delete()      
        except Exception as e:
            raise CustomAPIException(
                detail=repr(e))            
        else:
            print("proj clear success!")                