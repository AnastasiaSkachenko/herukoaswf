def binary_to_decimal(number):
    items = []
    decimal = 0
    number = str(number).strip()
    for num in number:
        items.append(int(num))
    items = items[::-1]
    for num,item in enumerate(items):
        decimal += item*(2**num)
    return decimal

def decimal_to_binary(number):
    binary = []
    while number >= 1 :
        change = number % 2
        binary.append(change)
        number = number // 2

    binary = binary[::-1]
    binary = map(str, binary)
    binary = ''.join(binary)
    binary = int(binary)

    return binary
def is_binary(number):
    flag = 0
    string = str(number)
    for i in string:
        if i != '0' and i != '1':
            flag = 1
    if flag == 1:
        return False
    else:
        return True

print(is_binary(10101))



