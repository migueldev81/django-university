from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializers
from .models import Student
from rest_framework import status
from django.http import Http404
    
class Student_APIView(APIView):
    
    #getAllStudents
    def get(self, request, format=None):
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data)
    
    #addStudent
    def Student(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Student_APIView_Detail(APIView):
    
    #ReqWithParams
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    #getStudent
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializers(student)  
        return Response(serializer.data)
    
    #updateStudent
    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #deleteStudent
    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Student_APIView_Querys(APIView):
    
    #ReqWithParams
    def get_object(self, *args):
        try:
            return Student.objects.get(name=args.name)
        except Student.DoesNotExist:
            raise Http404
    
    #getStudent
    def get(self, request, name, format=None):
        student = self.get_object(name)
        serializer = StudentSerializers(student)  
        return Response(serializer.data)