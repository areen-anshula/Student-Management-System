from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerialaizer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class StudentListCreate(APIView):
    def post(self, request):
        serializer = StudentSerialaizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerialaizer(students, many=True)
        return Response(serializer.data)

class StudentDetails(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)    
        serializer = StudentSerialaizer(student)  
        return Response(serializer.data)

    def put(self, request, pk):
        students = get_object_or_404(Student, pk=pk)    
        serializer=StudentSerialaizer(students, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)    
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    