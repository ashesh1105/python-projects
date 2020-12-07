from django.shortcuts import render

# Create your views here.
def index(request):
    # Let's create a context dictionary to try template filters with index.html!
    context_dict = {'text': 'hello world!', 'number': 50}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
