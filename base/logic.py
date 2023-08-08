def to_simple_fraction(list, number): 
    list.append(number[0] * number[2] + number[1])
    list.append(number[2])

    return list


def addition(number1, number2):
    numerator = number1[0] * number2[1] + number1[1] * number2[0]
    denominator = number1[1]*number2[1]
    return [numerator, denominator]


def subtraction(number1, number2):
    numerator = number1[0] * number2[1] - number1[1] * number2[0]
    denominator = number1[1] * number2[1]
    return [numerator, denominator]


def multiplication(number1, number2):
    numerator = number1[0]*number2[0]
    denominator = number1[1]*number2[1]
    return[numerator, denominator]


def division(number1, number2):
    numerator = number1[0]*number2[1]
    denominator = number1[1]*number2[0]
    return [numerator, denominator]


def to_mixed_fraction(list):
    if list[0] > list[1]:
        integer = list[0]//list[1]
        numerator = list[0]%list[1]
        denominator = list[1]
    else:
        integer = ''
        numerator = list[0]
        denominator = list[1]

    return [integer, numerator, denominator]


def reduction_of_fractions(list):
    item1 = list[0]
    item2 = list[1]
    for num in range(2, list[1]+1):
        first = list[0]%num
        second = list[1]%num
        if first == 0 and second == 0:
            item1 = list[0]/num
            item2 = list[1]/num

    return [int(item1), int(item2)]


list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_20 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
list_50 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42,
            44, 45, 46, 48, 49, 50]
list_100 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42,
            44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77,
            78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]

operators = ['+', '-', '*', '/']

def full_function_y(integer_1, integer_2, numerator_1, numerator_2, denominator_1, denominator_2, operator):
    answer = 'fuck'
    first_number = [int(integer_1), int(numerator_1), int(denominator_1)]
    second_number = [int(integer_2), int(numerator_2), int(denominator_2)]
    first_num = []
    second_num = []
    
    first_num = to_simple_fraction(first_num, first_number)
    second_num = to_simple_fraction(second_num, second_number)

    match operator:
        case 'addition' :
            answer = addition(first_num, second_num) 
        case 'substraction':
            answer = subtraction(first_num, second_num) 
        case 'multiplication':
            answer = multiplication(first_num, second_num) 
        case 'division':
            answer = division(first_num, second_num) 
        case '+' :
            answer = addition(first_num, second_num) 
        case '-':
            answer = subtraction(first_num, second_num) 
        case '*':
            answer = multiplication(first_num, second_num) 
        case '/':
            answer = division(first_num, second_num) 

 

    answer = reduction_of_fractions(answer)
    main_answer = to_mixed_fraction(answer) 

    if len(main_answer) == 2:
            numerator = main_answer[0]
            denominator = main_answer[1]
            integer = None
            context = {'integer': None, 'numerator': numerator, 'denominator': denominator}
    elif len(main_answer) == 3:
        integer = main_answer[0]
        numerator = main_answer[1]
        denominator = main_answer[2]
        if numerator == 0: 
            context = {'integer':integer, 'numerator': None, 'denominator': None}
        if numerator == denominator:
            context = {'integer': denominator, 'numerator': None, 'denominator': None}
        else:                
            context = {'integer':integer, 'numerator': numerator, 'denominator': denominator}
    return context