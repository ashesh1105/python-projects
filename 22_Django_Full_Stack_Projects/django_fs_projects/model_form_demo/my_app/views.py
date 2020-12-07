from django.shortcuts import render
# from my_app.models import User
from my_app.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # commit=True saves form data into DB
            return index(request)   # return index view of the request
        else:
            print("ERROR! FORM INVALID!")

    return render(request, 'my_app/users.html', { 'form': form })

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {'users': user_list}
#     return render(request, 'my_app/users.html', context=user_dict)

def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'my_app/help.html', context=helpdict)
