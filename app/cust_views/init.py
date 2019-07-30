from rest_framework.views import APIView
from rest_framework.response import Response
from ..cust_services import *
from ..library.control_flow import switch

class InitAPIView(APIView):
    def get(self, request, type, format=None):
        for case in switch(type):
            if case('user'):
                UserService.init_data()
                break
            if case('dept'):
                DeptService.init_data()
                break
            if case('proj'):
                ProjService.init_data()
                break
            # if case('all'):  # default, could also just omit condition or 'if True'
            else:
                InitService.init_data()
                break
        return Response(status=204)

    def delete(self, request, type, format=None):
        for case in switch(type):
            if case('user'):
                UserService.clear_data()
                break
            if case('dept'):
                DeptService.clear_data()
                break
            if case('proj'):
                ProjService.clear_data()
                break
            # if case('all'):  # default, could also just omit condition or 'if True'
            else:
                InitService.clear_data()
                break
        return Response(status=204)    
