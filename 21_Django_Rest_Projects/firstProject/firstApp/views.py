from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.
def employeeView(request):
    # emp = {
    #     'id': 123,
    #     'name': 'Ashesh',
    #     'sal': 1000000
    # }

    data = Employee.objects.all();

    # Since data is a query set, we need to convert it into a dictionary to return it
    # We can chose not send one ore more columns like id to UI
    response = {'employees': list(data.values('id','name','sal'))}

    # return JsonResponse(emp)
    return JsonResponse(response)
