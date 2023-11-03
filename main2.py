def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    var = 'Hello world'
    print(var)  # Press Ctrl+F8 to toggle the breakpoint.
    # Комментарий 1

    #print("Привет \" привет")
    # print('Привет " привет' )
    # print('Привет \' привет' )
    # print('привет \\' )
    # print('п\tр\tи\tв\tе\tт' )
    # print ("Результат:",5-5)
    # print ("Результат:",5-5)
    # print ("Результат:",5-5)
    # print ("Результат:",5+5)
    # print ("Результат:",5-5)
    # print ("Результат:",5*5)
    # print ("Результат:",5**2)
    # print ("Результат:",5/3)
    # print ("Результат:",5//3)
    # print ("Результат:", min(1,2,-5,17))
    # print ("Результат:", max(1,2,-5,17))
    # print ("Результат:", abs(-5))
    # print ("Результат:", pow(5,3))
    # print ("Результат:", round(5/3))
    # input("Введите свой возраст:")

    # Переменные
    number = 5
    #print (number)
    #number = 7
    #print (number)
    #del number
    #number = 8 #int - целое число
    #print (number)

    #qwer = 4.123 #float - числа с плавающей точкой
    #print (qwer)

    #world = "World" #string - строка
    #print(qwer, world)

    #booolean = True   #bool (либо Falce)

# Переменные должны быть одного формата.
    # Преобразование типа данных int, float в string
    #print(str(qwer) + world)
    #либо
    #num2 = "4" #string
    #print(num2 + world)

    # Преобразование формата string в int
    #print(int(num2) + number)

    #print(world + str(int(num2) + number))


    #Получаемые значения от пользователей

    # Результаты выводятся  как строки
#num1 = input ("ВВедите возраст 1:")
#num2 = input ("ВВедите возраст 2:")

    #Рузультаты выводятся как цклые числа, с ними можно производить математические операции
#num1 = int(input ("ВВедите возраст 1:"))
#num2 = int(input ("ВВедите возраст 2:"))

#print ("Result",num1 + num2)
#print ("Result",num1 - num2)
#print ("Result",num1 * num2)
#print ("Result",num1 / num2)
#print ("Result",num1 ** num2)
#print ("Result",num1 // num2)

#num1 = int(input ("ВВедите возраст 1:"))
#num2 = int(input ("ВВедите возраст 2:"))

    #Мат.действия с переменными. Сначала прибавляем к переменной, введеной пользователем число, н-р 5,
    # затем с полученным числом совершаем другие мат. действия
#num1 = num1 + 5 #либо
#num1 += 5 # возможно применять любые вычислительные действия
#print ("Result",num1 + num2)
#print ("Result",num1 - num2)
#print ("Result",num1 * num2)
#print ("Result",num1 / num2)
#print ("Result",num1 ** num2)
#print ("Result",num1 // num2)


#Условные конструкции
# if 5==5:
#     print ("YES")
#
# user_name=int(input("введите число 1:"))
# if user_name!=5: #варианты: >=, <=, ==, != (не равно)
#     print ("Мы молодцы") # ВАЖНО следить за отступами в куске кода
#     if user_name > 6:
#         print("Число не равно 5")
#
#         #Использование boolean как переменной
#         isHappy = False
#         if isHappy == False:
#             print('Happy')
#             # либо
#             if isHappy:
#                 print('Happy')
#                 # либо если условие не соответсвует
#             if not isHappy:
                # print('Happy')

# isHappy = True
# # data = int(input("введите число:"))
# # if not isHappy:
# #     print('Happy')
# # elif data == 2:# дополнительное условие (если первое условие не срабатывает,срабатывает второе условие,
# #     # если второе не срабатывает срабатывает третье). Доп.условий может быть несколько.
# #     print('Data is 2')
# # else:          #можно не использовать, тогда если предыдущие условия будут неверны, код не обработается
# #     print('Unhappy')

# isHappy = True
# data = int(input("введите число:"))
# if not isHappy and data==5:
#     print('Happy')
# elif data == 2:
#     print('Data is 2')
# else:
#     print('Unhappy')

# isHappy = True
# data = int(input("введите число:"))
# if isHappy or data==5:
#     print('Happy')
# elif data == 2:
#     print('Data is 2')
# else:
#     print('Unhappy')
#
# isHappy = True
# data = int(input("введите число:"))
# if isHappy and data==5:
#     print('Happy')
# elif data == 2:
# #     print('Data is 2')
# # else:
# #     print('Unhappy')
#
#
# # Тернарный оператор
#
# data = input()
# if data == "Seven":
#     number = 7
# else:
#     number = 0
# print(number)
#
# # Устанавливаем заначение 7 только в том случаи если data == "Семь", иначе уставливаем значение 0
# number = 7 if data == "Seven" else 0
# print(number)


# name = input()
# if name == "Женя":
#     number = 8
#     print("Женя выбрал число "+ str(number))
# else:
#     number = 13
#     print("Элина выбрала число" + str(number))

# #Тернарный оператор
# number = 8 if name == "Женя" else 0
# print(number)

#Циклы
# Работа с целыми числами int
# for perem in range(9): #цикл идет от 0 (по умолчанию) до 9(не включительно)
#     print(perem)
# for perem in range(1, 9): #цикл идет от 1 до 9 (не включительно)
#     print(perem)
# for perem in range(1, 9, 3): #цикл идет от 1 до 9(не включительно) с интервалом 3 (выводит 1,4,7)
#     print(perem)

# for perem in range(1, 9): #цикл идет от 1 до 9(не включительно) с интервалом 3 (выводит 1,4,7)
#     if perem == 7:
#         break #выходит из цикла при выполнении условия
#     print(perem)

# for perem in range(1, 9): #цикл идет от 1 до 9(не включительно) с интервалом 3 (выводит 1,4,7)
#     if perem == 7:
#         break
#     if perem % 2 == 0: #если наша переменная кратна 2
#         continue # пропускает итерацию, которая соответствует условию
#     print(perem)
#
#
# #Работа со строками
# for perem in ("Доброе утро!"):
#     print(perem * 3)

# count = 0
# for perem in ("Доброе утро!"):
#     if perem == "о":
#         count += 1
# print("Количество:", count)


# for my in ("JavaScript):
#     print (my)
#
# for my in ("JavaScript"):
#     if my == "p":
#         print ("ok")

# count = 0
# for my in ("PythonPythonPythonPython"):
#     if my == "P":
#         count += 1
# print ('Количество букв', count)

# usl = None
# for me in ("PythonPythonPythonPython"):
#     if me == "g":
#         usl = True
#         break
# else: usl = False
# print (usl)


# #Функции. Списки
# i = [9,8,7,6,5,4,43,3] # отсчет (индекс) элементов в листе начинается с 0
# print (i)
#
# #замена элемента листа
# i = [9,8.3, 'Elina']
# i [0] = 12
# print (i)
#
# # вывести один элемент листа
# i = [9,8.3]
# i [0] = 12
# print (i[0])
#
# #список в списке
# i = [9,8.3, ["Elina", 7]]
# i [0] = 12
# print (i[2])
# #либо
# print (i[-1]) #последний элемент из списка (обратный индекс)
#
# i = [9,8,7,6,5,4,43,3,["Elina", 7]] # отсчет (индекс) элементов в листе начинается с 0
# print (i [-1][0])
#
# #Добавление новых значений после создания списка
# i = [1,23,4,5]
# i.append(4100) #значение добавляется в конец. Можно вызывать любое количество раз любой тип данных
# i.append('Elina')
# i.append(True)
# print (i)
#
# #Помещение элемента на конкретное место (индекс) в листе
# i = [1,2,3,4,5,7]
# i.insert(5, 6) #указываем сначала индекс, затем через запятую значение элемента (любой тип данных)
# print(i)
#
# #Добавление нескольких элементов
# i = [1,2,3,4,5,7]
# i.extend(['Elina',15, False]) #добавляет в конец списка набор нескольких элементов
# print(i)
# #либо присваеваем вносимому списку переменню
# i = [1,2,3,4,5,7]
# g = ('Elina',15, False)
# i.extend(g) #добавляет в конец списка набор нескольких элементов
# print(i)
#
# #Сортировка элементов из списка
# i = [1,2,3,4,5,7,True,False] #False - присваивается индекс 0; True- присваивается индекс 1
# i.sort() #сортировка по возрастанию
# print(i)
#
# #Элементы в списке в обратном порядке
# i = [1,2,3,4,5,7,True,False]#Всегда! False - присваивается индекс 0; True- присваивается индекс 1
# i.reverse() #переворачивает список задом наперед кроме True,False
# print(i)
#
# #удаление элементов
# i = [1,2,3,4,5,7,True,False]
# i.pop() #удаление последнего элемента
# i.pop() #можно вызывать несколько раз, каждый раз удаляется последний элемент
# i.pop(-1) #можнно вводить ИНДЕКС того элемента, который хотим удалить
# print(i)
#
# i = [1,2,3,4,5,7,True,False]
# i.remove(7) #удаляет любой прописанный элемент списка. Прописываем ЗНАЧЕНИЕ
# print(i)
#
# i = [1,2,3,4,5,7,True,False]
# i.clear() #удаляет весь список
# print(i)
#
# #Посчитать количество элементов с конкретным значением
# i = [1,2,3,4,5,5,5,7,True,False]
# print(i.count(5)) #выводит количество элементов со значением 5
#
# #Длина всего списка
# i = [1,2,3,4,5,5,5,7,True,False]
# print(len(i))
#
# #Перебрать весь список
# i= [1,2,3,4,'Elina', True]
# for el in i:
#      print(el)
#
#
# i= [1,2,3,4,int('Elina'), True]
# for el in i:
#     if el > 2:
#         print(el)
#
# i= ['ElinaGazinaElinaGazina']
# for el in i:
#     if el == 'z':
#         print(el)
#     else: print("not el")


#Кортеж
#записывается через круглые скобки
#тотже смписок только элементы нельзя изменять,удалять,добавлять элементы, переприсваивать значения
#весят меньше, чем списки
#используются для передачи данных, пользователь не может изменить набор списка
i= (1,2,3,4,'Elina', True)
print(i)
# либо
i= 1,2,3,4,'Elina', True
print(i)

i= (1) # один элемент это не кортеж
print(i)

i= (1,) # один элемен с запятой это кортеж
print(i)
# либо
i= 1, # один элемен с запятой это кортеж
print(i)



i= (1,2,3,4,'Elina', True)
print(i[1]) #вывести элемент также как и в спискав в [индекс элемента]

#Функции кортежей
#посчитать количест во элементов с конкретным значением
i= (1,2,3,4,'Elina', True)
print(i.count(2))
#посчитать количест во элементов в кортеже
i= (1,2,3,4,'Elina', True)
print(len(i))

i= (1,2,3,4,'Elina', True)
for el in i:
    print(el)

#Преобразовать список в кортеж
i = [1,2,3,4,5,7]
f=tuple(i)
print(i)
print(f)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

