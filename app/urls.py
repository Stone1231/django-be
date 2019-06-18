from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/<int:id>', views.UserAPIView.as_view()),
    path('users', views.UserListAPIView.as_view()),
    path('depts/<int:id>', views.DeptAPIView.as_view()),
    path('depts', views.DeptListAPIView.as_view()),
    path('projs/<int:id>', views.ProjAPIView.as_view()),
    path('projs', views.ProjListAPIView.as_view()),    
    path('init/<str:type>', views.InitAPIView.as_view()),  
]