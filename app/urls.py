from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/<int:id>', views.UserAPIView.as_view()),
    path('user', views.UserListAPIView.as_view()),
    path('dept/<int:id>', views.DeptAPIView.as_view()),
    path('dept', views.DeptListAPIView.as_view()),
    path('proj/<int:id>', views.ProjAPIView.as_view()),
    path('proj', views.ProjListAPIView.as_view()),    
    path('init/<str:type>', views.InitAPIView.as_view()),  
]