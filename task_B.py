# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

def dict_coef(string):
    string = string.replace(' ', '').replace('-', '+-').replace('=0', '').split('+')
    if string[0] =='':
        string.pop(0)
    for i in range(len(string)):
        string[i] = string[i].replace('*', '').split('x')
        if len(string[i]) < 2:
            string[i].append('0')
        if string[i][1] == '':
            string[i][1] = '1'
   
    dict = {int(string[i][1]): int(string[i][0]) for i in range(len(string))}

    new_dict = {i: 0 for i in range(int(string[0][1]), -1, -1)}  

    new_dict.update(dict)    

    return (new_dict) 

def result_equation(dict1, dict2):
    
    differ_dict = {}
    if len(dict1) > len(dict2):
        for i in range(len(dict1)-1, len(dict2)-1, -1):
            differ_dict[i] = 0
        dict2 = {**differ_dict, **dict2}
    else:
        for i in range(len(dict2)-1, len(dict1)-1, -1):
            differ_dict[i] = 0
        dict1 = {**differ_dict, **dict1}

    result = {}
    for i in range(len(dict2)-1, -1, -1):
        result[i] = dict1[i] + dict2[i]

    return(result)

def print_equation(dict):

    str_equation = ''
    
    for key in range(len(dict)-1, -1, -1):
        if key == len(dict)-1:
            if dict[key] == 1: 
                str_equation += f'x^{key}'
            elif dict[key] == -1:
                str_equation += f'- x^{key}'
            else:
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

string1 = open("homework/hw4/eq1.txt")
equation1 = string1.read()
string1.close()

string2 = open("homework/hw4/eq2.txt")
equation2 = string2.read()
string2.close()

print(equation1)
my_dict1 = dict_coef(equation1)
print(equation2)
my_dict2 = dict_coef(equation2)

print('Сумма многочленов равна:')  
print(print_equation(result_equation(my_dict1, my_dict2)))