from django.shortcuts import render
from .forms import Count, ConverterForm
from .logic import *
import random
from .logic_ import binary_to_decimal, decimal_to_binary, is_binary
from django.contrib import messages

list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_20 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
list_50 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42,
            44, 45, 46, 48, 49, 50]
list_100 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42,
            44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77,
            78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]

operators = ['+', '-', '*', '/']


def home(request):
    form = Count()
    context = {}
    if request.method =='POST':
        form = Count(request.POST) 
        integer_1, integer_2 = 0,0
        
        numerator_1 = request.POST.get('numerator_1', False)
        denominator_1 = request.POST.get('denominator_1', False)

        operator = request.POST.get('operator', False)
        
        numerator_2 = request.POST.get('numerator_2', False)
        denominator_2 = request.POST.get('denominator_2', False)
        try:
            context = full_function_y(integer_1, integer_2, numerator_1, numerator_2, denominator_1, denominator_2, operator) 
        except ValueError:
            messages.warning(request, 'Please fill first all fields')
     
            
    return render(request, 'index.html', context)


def mixed_fraction(request):
    form = Count()
    context = {}
    if request.method =='POST':
        form = Count(request.POST) 
        integer_1 = request.POST.get('integer_1', False)
        
        numerator_1 = request.POST.get('numerator_1', False)
        denominator_1 = request.POST.get('denominator_1', False)

        operator = request.POST.get('operator', False)
        
        integer_2 = request.POST.get('integer_2', False)
        numerator_2 = request.POST.get('numerator_2', False)
        denominator_2 = request.POST.get('denominator_2', False)

         
        try:
            context = full_function_y(integer_1, integer_2, numerator_1, numerator_2, denominator_1, denominator_2, operator) 
        except ValueError:
            messages.warning(request, 'Please fill first all fields')

    return render(request, 'base/mixed_fraction.html', context)

def random_simple(request):
    context = {}
    operator = '+'
    range_n = list_10
    form = Count()
    if request.method =='POST':
        form = Count(request.POST) 
        if 'Random numbers' in request.POST:
            range = request.POST.get('range')
            integer_1 = 0
            integer_2 = 0 
            range = int(range)

            match range:
                case 10:
                    range_n = list_10
                case 20:
                    range_n = list_20
                case 50:
                    range_n = list_50
                case 100:
                    range_n = list_100

            numerator_1 =  random.choice(range_n)
            numerator_2 = random.choice(range_n)
            denominator_1 = random.choice(range_n)
            denominator_2 = random.choice(range_n)
            operator = random.choice(operators)

            counted = full_function_y(integer_1, integer_2, numerator_1, numerator_2, denominator_1, denominator_2, operator)

            context = {'numerator_1': numerator_1, 'numerator_2':numerator_2, 'denominator_1': denominator_1, 'denominator_2': denominator_2, 'operator':operator} 
            context['integer'] = counted['integer']
            context['numerator'] = counted['numerator']
            context['denominator'] = counted['denominator']   
            print(context)
    return render(request, 'base/random.html', context)



def random_mixed(request):
    context = {}
    operator = '+'
    range_n = list_10
    form = Count()
    if request.method =='POST':
        form = Count(request.POST) 
        if 'Random numbers' in request.POST:
            range = request.POST.get('range')
            range = int(range)

            match range:
                case 10:
                    range_n = list_10
                case 20:
                    range_n = list_20
                case 50:
                    range_n = list_50
                case 100:
                    range_n = list_100

            integer_1 = random.choice(range_n)
            integer_2 = random.choice(range_n)
            numerator_1 =  random.choice(range_n)
            numerator_2 = random.choice(range_n)
            denominator_1 = random.choice(range_n)
            denominator_2 = random.choice(range_n)
            operator = random.choice(operators)

            counted = full_function_y(integer_1, integer_2, numerator_1, numerator_2, denominator_1, denominator_2, operator)

            context = {'integer_1': integer_1, 'integer_2':integer_2, 'numerator_1': numerator_1, 'numerator_2':numerator_2, 'denominator_1': denominator_1, 'denominator_2': denominator_2, 'operator':operator} 
            context['integer'] = counted['integer']
            context['numerator'] = counted['numerator']
            context['denominator'] = counted['denominator']   
            print(context)

    return render(request, 'base/random_mixed.html', context)


def convertor(request):

    if request.method == 'POST':
        form = ConverterForm()
        system = request.POST.get('system', False)
        number = request.POST.get('number', False)

        print(system, number)
        try:
            number = int(number)
        except ValueError:
            messages.warning(request, 'Please enter the number')

        if system == 'binary' and number !='':
            if is_binary(number):
                answer = binary_to_decimal(number)
                messages.warning(request, f'The number {number} in decimal system is {answer}. Thank you for using this site!')
            else:
                messages.warning(request, f'The number {number} is not binary, in binary number can be only 1 or 0')

        elif system == 'decimal' and number !='':
            answer = decimal_to_binary(number)
            messages.info(request, f'The number {number} in binary system is {answer}. Thank you for using this site!')



    return render(request, 'base/convertor.html')
