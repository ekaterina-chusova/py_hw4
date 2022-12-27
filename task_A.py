# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 
# 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

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

k = int(input("Введите значение натуральной степени многочлена: "))

coefficient = create_coefficients(k)
print(coefficient)
print(print_equation(coefficient, k)) 