from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# LOGIN / LOGOUT related imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
# Below was deprecated from Django 2.0 onwards. User django.urls instead!
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You're logged in, Nice!")

# Below decocator helps this function to be called only by users who are logged in!
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # set_password allows hashing the password based on auth details in settings.py file
            user.set_password(user.password)
            user.save()

            # Dealing with extra attributes now
            # We do not want to save this prfile with our user yet!
            profile = profile_form.save(commit=False)

            # sets 1:1 relationship with user with profile and user we have from user_form
            profile.user = user

            # Check if user provided profile picture
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # print('registered: ' + str(registered))

    return render(request, 'basic_app/registration.html',
                            {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Below automatically authenticates the user for us! Thank you Django! :)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                # Send the user somewhere now
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active!")
        else:
            print('Someone tried to login and failed!')
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'basic_app/login.html', {})
