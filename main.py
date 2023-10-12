#Первое задание: нужно найти простое число
num = int(input())
if num <= 1:
   print('Число не простое')
else:
   for i in range(2, num):
       if num % i == 0:
          print('Число не простое')
          break
   else:
       print('Число просто')

#Второе задание: найти самoe большоe
#mas = (6,56,7,43,5,6,7,5,3,3,7)
#a = mas[0]
#for i in mas:
#    if i > a:
#        a = i
#print(a)

#Третье задание: найти наибольшее число в массиве
# mas = [1,6,3,2,5,6,2,3,56,5,4,3,3,45,3,2,2,1,2,3,4,57,9,0,9,87,543,4, -3, -333]
# maximum = mas[0]
# for i in mas:
#     if i > maximum:
#         maximum = i
# print(maximum)

# Четвертое задание: фибоначчи
# fib = int(input())
# a = 1
# b = 1
# print(a, b, end=' ')
# for i in range(2, fib):
#    a,b = b, a + b
#    print(b, end=' ')