from django.shortcuts import render

# Create your views here.

def input(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))

    context = {
        'num1' : num1,
        'num2' : num2,
        'mult_num' : num1 * num2,
        'sub_num' : num1 - num2,
    }

    if num2 != 0:
        context['div_num'] = num1 / num2

    return render(request, 'calculators/result.html', context)