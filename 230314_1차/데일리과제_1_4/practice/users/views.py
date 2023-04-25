from django.shortcuts import render

# Create your views here.

menus = ['fish_and_chips', 'chicken', 'pasta', 'pizza', 'rice', 'kimchi']
users= []

def hw1(request):

    context = {
        'menus' : menus,
    }

    return render(request, 'users/hw1.html', context)

def hw2(request):

    context = {
        'users' : users,
    }
        
    return render(request, 'users/hw2.html', context)

def hw3(request):

    context = {
        'menus' : menus,
    }

    return render(request, 'users/hw3.html', context)

def hw4(request):
    return render(request, 'users/hw4.html')

def hw5(request):

    today = ''

    return render(request, 'users/hw5.html', {'today':today})