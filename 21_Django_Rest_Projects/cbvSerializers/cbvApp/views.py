from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework import viewsets

# Below import is not needed since we are using viewsets now!
# from rest_framework import generics

# Below import were already not needed since we started using generics!
# from rest_framework import mixins

# Below imports were not needed since we started using mixins!
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from django.http import Http404

# viewsets simplify our code for ReSTful APIs even more than generics or mixins do!
# Both primary_key and non-primary_key based operations can now be supported with just one class
# below and that too with just 2 lines of code in it!!
# With viewsets, we do need to configure Routes, so urls.py now look different! Check it out!
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

'''
Django Rest Framework (DRF) Generics:
Mixins helps us reduce the number of lines of code we need to write to create endpoints. But we still have to
repeat handler methods and action methods across the ReSTful APIs we create. This is where DRF Generics help us.
They give us a set of classes we can use which help further reduce number of lines of code we need to write.
They give us classes we can use for it like:
- CreateAPIView
- ListAPIView
- RetrieveAPIView
- DestroyAPIView
- UpdateAPIView

They give us combination classes as well to support all the non-id and id-based operations, like:
- ListCreateAPIView
- RetrieveUpdateAPIView
- RetrieveDestroyAPIView
- RetrieveUpdateDestroyAPIView

You can extend any of above classes based on what you’re intending to do!
For example, below two classes on your view can support list all, create, retrieve specific object,
update and delete the students!! So, say, we just need to List Students and not Create them, we will
import generics.ListAPIView and not generics.ListCreateAPIView. Similarly, if we do not need delete
functionality, on StudentDetail class, we will import generics.RetrieveUpdateAPIView and not the
generics.RetrieveUpdateDestroyAPIView !!
'''
# Commenting our below code as well since we will use viewsets and not (even) generics anymore!
'''
# Class for non-primary-key based operations
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Class for primary-key based operations
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''

# Mixin example. Although using generics (above) is much better as they help keep code DRY even more!
# Class for non-primary-key based operations
'''
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request,pk)

    def put(self, request, pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.destroy(request,pk)
'''

# Since we're using mixins (above), we no longer need to write so much code for various models. For example, we provide
# serializer once for non-primary-key or primary_key based operations (classes) and DRF (Django Rest Framework) can
# reuse the serializer for variaous methods in the class, like get, post, etc. Also, we do not need to manually
# save the data, DRF does it for us, all we need to do is invoke the action methods that come with mixins classes we
# inherit the two classes from, like ListModelMixin, RetrieveModelMixin, etc.!
'''
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
'''
