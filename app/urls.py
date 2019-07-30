from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('error', views.error),
    path('user/<int:id>', views.UserAPIView.as_view()),
    path('user', views.UserListAPIView.as_view()),
    path('user/ufile', views.UserImgAPIView.as_view()),
    path('user/query', views.UserQueryListAPIView.as_view()),
    path('dept/<int:id>', views.DeptAPIView.as_view()),
    path('dept', views.DeptListAPIView.as_view()),
    path('proj/<int:id>', views.ProjAPIView.as_view()),
    path('proj', views.ProjListAPIView.as_view()),    
    path('init/<str:type>', views.InitAPIView.as_view()),  
    path('auth/login', views.LoginAPIView.as_view()),  
    path('auth', views.AuthAPIView.as_view()),  
    path('auth/anonymous', views.AnonymousAPIView.as_view()),  
    path('file/ufiles', views.UploadsAPIView.as_view()),
    path('file/ufile', views.UploadAPIView.as_view()),
    path('file/ufile2', views.Upload2APIView.as_view()),
]