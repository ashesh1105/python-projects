from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class StudentList(APIView):

    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self,request):
        # We need to tell where our serializer will get data from?
        # data is an attribute of serializer
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):

    # Since in Class Based View, we do not have a method like student_detail() in Function Based View
    # Below built in method comes handy for us to grab the object based on Primary Key!
    def get_object(self,pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            # You can simply raise the exception once you import it!
            # return Response(status=status.HTTP_404_NOT_FOUND)
            raise Http404

    def get(self,request,pk):
        # You can now use the get_object method above to grab the object!
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
