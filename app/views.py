from .cust_views import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view()
def index(request):
    return Response("Hello, it is api")
