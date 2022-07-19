from django.urls import path
from .views import *
app_name = 'student'
urlpatterns = [
    path('v1/student', Student_APIView.as_view()), 
    path('v1/student/<int:pk>/', Student_APIView_Detail.as_view()),
    
]