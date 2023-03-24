from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'name' : 'aiden',
        'age' : 21,
    }

    return render(request, 'myapps/index.html', context)