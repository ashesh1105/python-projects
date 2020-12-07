from django import template

register = template.Library()

# This is how we can create our own custom template filters. Check out the built-in ones before creating your own!
# Remember this file must be added under <app_name>, which is basic_app in our case -> 'templatetags' folder and we need to mark
# templatetags as a package by adding an emplty __init__.py file in it!
# Adding below decorator to our filter function is newer and better way to register our function!
@register.filter(name='cut')
def cut(value,arg):
    '''
    This cuts out all values of "arg" from a string
    '''
    return value.replace(arg, '')

# Now, register our function with name as we want this to be called from templates
# Note: This is older way of regitering our custom filters. We now do it by annotating our method with decorator for it, as above!
# register.filter('cut', cut)
