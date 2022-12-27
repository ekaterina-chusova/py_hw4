# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import random

def create_coefficients(n):
    coef = {}
    for i in range(n, -1, -1):
        if i == n:
            while True:
                num = random.randint(-100, 100)
                if num != 0:
                    break
            coef[i] = num
        else:
            coef[i] = random.randint(-100, 100)   
    return(coef)

def print_equation(dict, n):

    str_equation = ''
    
    for key in range(n, -1, -1):
        if key == n:
            str_equation += str(dict[key]) + f'*x^{key}'        
        elif dict[key] == 0:
            str_equation = str_equation
        elif dict[key] == 1 and key != 0: 
            str_equation += f' + x^{key}'
        elif dict[key] == -1 and key != 0: 
            str_equation += f' - x^{key}'    
        elif key == 0: 
            str_equation += f' + {dict[key]}'
        else:
            str_equation += ' + ' + str(dict[key]) + f'*x^{key}'
            
    str_equation = str_equation.replace('+ -', '- ') + ' = 0'        
    return(str_equation)

def result_equation(dict1, n1, dict2, n2):
    
    differ_dict = {}
    if n1 > n2:
        for i in range(n1, n2, -1):
            differ_dict[i] = 0
        dict2 = {**differ_dict, **dict2}
        count = n1
    else:
        for i in range(n2, n1, -1):
            differ_dict[i] = 0
        dict1 = {**differ_dict, **dict1}
        count = n2
    
    result = {}
    for i in range(count, -1, -1):
        result[i] = dict1[i] + dict2[i]

    return(result, count) 

k1 = int(input("Введите значение натуральной степени первого многочлена: "))
k2 = int(input("Введите значение натуральной степени второго многочлена: "))

coefficient1 = create_coefficients(k1)
# print(coefficient1)
print(print_equation(coefficient1, k1))

coefficient2 = create_coefficients(k2)
# print(coefficient2)
print(print_equation(coefficient2, k2)) 

new_equation, count = result_equation(coefficient1, k1, coefficient2, k2)  
# print(new_equation)

print('Сумма многочленов равна:')  
print(print_equation(new_equation, count))

