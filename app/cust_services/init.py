from django.db import transaction
from . import *


class InitService(object):
    @staticmethod
    def init_data():
        with transaction.atomic():
            DeptService.init_data()
            ProjService.init_data()
            UserService.init_data()
            AuthService.init_data()
            FileService.clear("img")
        print("dept init success!")

    @staticmethod
    def clear_data():
        with transaction.atomic():
            UserService.clear_data()
            DeptService.clear_data()
            ProjService.clear_data()
            AuthService.clear_data()
            FileService.clear("img")
        print("dept init success!")
