# Найдите сумму цифр трехзначного числа.
# num = int(input('Введите трехзначноe число: '))
# sum = 0
# while num > 0:
#     sum = sum + (num % 10)
#     num //= 10
# print('Сумма цифр числа равно: ', sum)


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# s = int(input('Общее количество журвликов: '))
# k = s / 3 * 2
# p = k / 2 / 2
# c = p
# print('=================================')
# print('Катя сделала', k, 'журавликов')
# print('Петя сделал', p, 'журавликов')
# print('Сережа сделала', c, 'журавликов')


# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# numticket = int(input('Введите номер билета: '))
# sum1 = 0
# sum2 = 0
# while numticket >= 999:
#     sum1 = sum1 + (numticket % 10)
#     numticket //= 10
# while numticket > 0:
#     sum2 = sum2 + (numticket % 10)
#     numticket //= 10
# print('==============================')
# if sum1 == sum2:
#     print('Счасливый билет')
# else:
#     print('Повезет в следующий раз')
# print('==============================')


# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# n = int(input('Количество плиток в длину: '))
# m = int(input('Количество плиток в ширину: '))
# k = int(input('Количество долек: '))
# print('==============================')
# if k % n == 0 or k % m == 0:
#     print('YES')
# else:
#     print('NO')



# Напишите программу, которая вводит с клавиатуры номер месяца и день, и определяет, сколько дней осталось до Нового года. 
# При вводе неверных данных должно быть выведено сообщение об ошибке. Считается, что год невисокосный.

month = int(input('Введите месяц: '))
day = int(input('Введите день: '))
sumday = 0

if ((month == 1 or month == 3 or month == 12 or month == 5 or month == 7 or month == 8 or month == 10) and (day > 31 or day < 1)) or ((month == 2) and (day>29 or day < 1)) or ((month == 4 or month == 6 or month == 9 or month == 11) and (day > 30 or day < 1)) or (month <= 0) or (month > 12):
    print('Ошибка')

if month == 1:
    sumday = 0
elif month == 2:
    sumday = 31
elif month == 3:
    sumday = 31 + 28
elif month == 4:
    sumday = 31 + 28 + 31
elif month == 5:
    sumday = 31 + 28 + 31 + 30
elif month == 6:
    sumday = 31 + 28 + 31 + 30 + 31
elif month == 7:
    sumday = 31 + 28 + 31 + 30 + 31 + 30
elif month == 8:
    sumday = 31 + 28 + 31 + 30 + 31 + 30 + 31          
elif month == 9:
    sumday = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
elif month == 10:
    sumday = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 
elif month == 11:
    sumday = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
elif month == 12:
    sumday = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30

print('Дней до нового года осталось: ', 365 - (sumday + day))