from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessRecord

# Create your views here.
def index(request):

    # return HttpResponse("Hello from Django Full Stack - first_app!")
    # my_dict = {'insert_me': "Hello, I am coming from first_app/index.html!"}
    # return render(request, 'first_app/index.html', context=my_dict)

    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}

    return render(request, 'first_app/index.html', context=date_dict)

def help(request):
    help_insert = {'help_insert': "Help Page"}
    return render(request, 'first_app/help.html', context=help_insert)
