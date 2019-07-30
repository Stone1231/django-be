from rest_framework.exceptions import APIException, _get_error_details
from rest_framework import status
from django.utils.encoding import force_text

class CustomAPIException(APIException):
    # status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    # default_detail = 'A server error occurred.'

    def __init__(self, detail, code=None, status_code=500):
        if status_code is not None:
            self.status_code = status_code
        if code is not None:
            detail = {code: force_text(detail)}
 
        self.detail = _get_error_details(detail, code)
        

    def add(self, code, detail):
        if code is not None:
            self.detail[code] = force_text(detail)
            self.detail = _get_error_details(self.detail, code)