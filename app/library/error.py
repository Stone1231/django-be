from rest_framework.views import exception_handler
from rest_framework import status
from django.http import JsonResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is None:
        return JsonResponse(
            {
                'msg': exc.args[0],
                'state': '-1'
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
