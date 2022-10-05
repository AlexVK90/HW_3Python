#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#Пример:

#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def sum(s):
    sum = 0
    for i in range (1, len(s), 2):
        sum += s[i]
    return sum

def list(n):
    list = []
    for i in range(n):
        list.append(randint(1, n))
    return list

n = int(input('Введите количество чисел: '))
numbers = list(n)
print(numbers)

result = sum(numbers)

print(f'Сумма элементов, стоящих на нечетной позиции = {result}')





#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


s = [2, 3, 4, 5, 6]
#s = [2, 3, 4, 5]

def multi_pairs(s):
    result= []
    j = (-1)
    if len(s)%2 != 0:
        for i in range (int(len(s)/2 +1)):
            result.append(s[i]*s[j])
            j+=(-1)
    else:
        for i in range (int(len(s)/2)):
            result.append(s[i]*s[j])
            j+=(-1)

    return(result)

print(multi_pairs(s))





#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем

#*Пример:*

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19


s = [1.1, 1.2, 3.1, 5, 10.01]

new_s=[]

for i in s:
    new_s.append(i - int(i))

min = 1    
    
for i in new_s:
    if i != 0 and i < min:
            min = i
            
print(round (max(new_s) - min, 3))






#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

n = int(input('Введите десятичное число: '))

def dec(n):
    number = ''
    while n > 0:
        number = str(n%2) + number
        n = n//2

    return(number)

print(f'Число {n} в двоичном исчислении = {dec(n)}')
        






#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#Пример:

#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]



def negafibonachi(n):
    list1 = [0,0]
    list1[0] = 0
    list1[1]= 1
    
    list2= []
    
    for i in range(2, n +1):
        x = list1[i-1] + list1[i-2]
        list1.append(x)
    
    l = len(list1) -1 
    
    for i in range(len(list1) -1):
        
        if (l - i) % 2 == 0:
            j = - list1[l - i]
            list2.append(j)
        else:
            j = list1[l - i]
            list2.append(j)
            
    return list2 + list1          
            
            
n = int(input('Введите число: '))

print(negafibonachi(n))