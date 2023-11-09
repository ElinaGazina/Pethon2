def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    var = 'Hello world'
    print(var)  # Press Ctrl+F8 to toggle the breakpoint.
    # Чать 3. Базовые операции
    # print("Привет \" привет")
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

    # Часть 4.Переменные
    number = 5
    # print (number)
    # number = 7
    # print (number)
    # del number
    # number = 8 #int - целое число
    # print (number)

    # qwer = 4.123 #float - числа с плавающей точкой
    # print (qwer)

    # world = "World" #string - строка
    # print(qwer, world)

    # booolean = True   #bool (либо Falce)


# Переменные должны быть одного формата.
# Преобразование типа данных int, float в string
# print(str(qwer) + world)
# либо
# num2 = "4" #string
# print(num2 + world)

# Преобразование формата string в int
# print(int(num2) + number)

# print(world + str(int(num2) + number))


# Получаемые значения от пользователей

# Результаты выводятся  как строки
# num1 = input ("ВВедите возраст 1:")
# num2 = input ("ВВедите возраст 2:")

# Рузультаты выводятся как цклые числа, с ними можно производить математические операции
# num1 = int(input ("ВВедите возраст 1:"))
# num2 = int(input ("ВВедите возраст 2:"))

# print ("Result",num1 + num2)
# print ("Result",num1 - num2)
# print ("Result",num1 * num2)
# print ("Result",num1 / num2)
# print ("Result",num1 ** num2)
# print ("Result",num1 // num2)

# num1 = int(input ("ВВедите возраст 1:"))
# num2 = int(input ("ВВедите возраст 2:"))

# Мат.действия с переменными. Сначала прибавляем к переменной, введеной пользователем число, н-р 5,
# затем с полученным числом совершаем другие мат. действия
# num1 = num1 + 5 #либо
# num1 += 5 # возможно применять любые вычислительные действия
# print ("Result",num1 + num2)
# print ("Result",num1 - num2)
# print ("Result",num1 * num2)
# print ("Result",num1 / num2)
# print ("Result",num1 ** num2)
# print ("Result",num1 // num2)


# Часть 5.Условные конструкции
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
#
#
#
# Часть 6.Циклы
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
#
#
#
#  #Часть 7.Функции. Списки
#  #Заключается в квадратные скобки
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
# # i= [1,2,3,4,int('Elina'), True]
# # for el in i:
# #     if el > 2:
# #         print(el)
#
# i= ['ElinaGazinaElinaGazina']
# for el in i:
#     if el == 'z':
#         print(el)
#     else: print("not el")
#
#
#
# # Часть 9.Кортеж
# # записывается через круглые скобки
# # тотже смписок только элементы нельзя изменять,удалять,добавлять элементы, переприсваивать значения
# # весят меньше, чем списки
# #используются для передачи данных, пользователь не может изменить набор списка
# i= (1,2,3,4,'Elina', True)
# print(i)
# # либо
# i= 1,2,3,4,'Elina', True
# print(i)
#
# i= (1) # один элемент это не кортеж
# print(i)
#
# i= (1,) # один элемен с запятой это кортеж
# print(i)
# # либо
# i= 1, # один элемен с запятой это кортеж
# print(i)
#
# i= (1,2,3,4,'Elina', True)
# print(i[1]) #вывести элемент также как и в спискав в [индекс элемента]
#
#
# #Функции кортежей
# i= (1,2,3,4,'Elina', True)
# print(i.count(2)) #посчитать количество элементов с конкретным значением
#
# i= (1,2,3,4,'Elina', True)
# print(len(i)) #посчитать количест во элементов в кортеже
#
# i= (1,2,3,4,'Elina', True)
# for el in i:
#     print(el)
#
# #Преобразовать список в кортеж
# i = [1,2,3,4,5,7]
# f=tuple(i)
# print(i)
# print(f)



# #Часть 8. Функции строк
# i = ('hello')
# print(i[1]) # вывести элемент (указать индекс)
#
# i= ('hello')
# print (len(i)) # вывести количество элементов
#
# i = ('hello')
# print (i.count('l')) # вывести количество элементов (указать, какой именно элемент)
#
#
# #Работа с регистрами
# i = ('hello')
# print (i.upper()) # выводит все элементы заглавными буквами
#
# i = ('hello')
# print (i.isupper()) # выводит булево - есть ли в строке заглавные буквы
#
# i = ('hello')
# print (i.lower()) # выводит все элементы прописными буквами
#
# i = ('hello')
# print (i.islower()) # выводит булево - есть ли в строке прописные буквы
#
# i = ('Hello')
# print (i.capitalize()) # выводит первый элемент как заглавную букву, последующие как прописные
#
# i=('Hello')
# print (i.find('e')) #выводит индекс указанного элемента, можно передавать только один элемент в одном запросе
#
# i=("Hello,Hello,Hello")
# print(i.split(",")) #разбить строчку запятой и получить список из нескольких элементов (элементы строки изнчально должны быть перечислены через запятую)
#
# i=("футбол,баскетбол, врлейбол") #вводим переменную и присвяиваем ей знчение split ...
# p=(i.split(','))
# print(p[1]) # ...и выводим конкретный элемент из списка по индексу
# #
#
# #Срезы - вывод несколько элементов из стороки
# i = ('Footboll')
# print(i[0:4]) #указываем начальный и конечный индекс элемента, котрый нужно вывести
#
# i = ('Footboll')
# print(i[4:8]) #указываем начальный индекс элемента (не включается в вывод) и конечный индекс элемента, котрый нужновывести
# # либо если нужно вывести до конца строки
# i = ('Footbool')
# print(i[4:])
# # либо использовать обратный отсчет
# i = ('Footboll')
# print(i[4:-1])
#
# # можно указать шаг
# i = ('Footboll')
# print(i[0:-1:2]) #через еще одно двоеточие указывается шаг
#
# #работа со списками
# list = [1, "Odin", 1.1, True]
# print(list[2:]) #вывести элементы списка начиная со второго до конца
#
# list = [1, "Odin", 1.1, True]
# print(list[0:-1]) # вывести все элементы списка кроме последнего
#
# list = [1, "Odin", 1.1, True]
# print(list[0::3]) #вывести все элементы списка от начала до конца и интервалом 3
#
# list = [1, "Odin", 1.1, True]
# print(list[::-1]) #перевернутый список



#     #Часть 10.Словари
#     #обязательно указывать ключ
#     #в фигурных скобках
#     #всегда есть ключ и его знчаение
#     #в качестве ключа можно использовать строки, кортежи, !!!но не списки!!!
# i= {"name": "Elina", "cantry": "RU", "profession": "QA"}
# print(i["name"]) #обращаемся по нужному нам ключу
#  #либо
# i= dict(name="Elina", cantry="RU", profession="QA")
# print(i["name"])
#
#
#  #перебрать словарь
# i= dict(name="Elina", cantry="RU", profession="QA")
# for key in i:  #если создается только одна переменная, то ввыводятся только ключи
#     print(key)
# #
# #     print(i.items()) #получаем список в которм каждый элемент это кортеж из "ключ:значение"
#
# for key, val in i.items():  #создаем 2 переменные и включаем функцию items
#     print(key, '-', val)

#
# # Функции при работе со словорями
# i= dict(name="Elina", cantry="RU", profession="QA")
# print(i.get("cantry")) #вывести значение равное заданному ключу аналогично выводу через print(i["cantry"])
#
# i= dict(name="Elina", cantry="RU", profession="QA")
# i.clear()  #удалить весь словарь
# # print(i)
#
# i = dict(name="Elina", cantry="RU", profession="QA")
# i.pop("name")  # удалить элемент по ключу
# print(i)
#
# i = dict(name="Elina", cantry="RU", profession="QA")
# i.popitem()  # удалить последний элемент "ключ:значение" из словаря
# print(i)
#
# i = dict(name="Elina", cantry="RU", profession="QA")
# print(i.keys())  # выводит только ключи
#
# i = dict(name="Elina", cantry="RU", profession="QA")
# print(i.values())  # выводит только значения
#
# i = dict(name="Elina", cantry="RU", profession="QA")
# print(i.items())  # выводит список элементами которого является кортеж "ключ:значение"
#
# # i.update() #обновление значений
# # либо
# i["cantry"] = "IT"
# print(i.items())
#
 #Описание человека
 #Задание: узнать улицу на которой живет Элина
# per = \
#     {
#         "user_1":
#             {
#                 "name": "Elina",
#                 "last_name": "Gazina",
#                 "age": 32,
#                 "profession": "QA",
#                 "adres": ["Ufa", "Inter.str", 27]
#             },
#         "user_2":
#             {
#                 "name": "Rinat",
#                 "last_name": "Gazin",
#                 "age": 36,
#                 'profession': "Engineer",
#                 "adres": ["Ufa", "Inter.str", 27]
#             },
#         "user_3":
#             {
#                 "name": "Ivan",
#                 "last_name": "Ivanov",
#                 "age": 30,
#                 'profession': "QA",
#                 "adres": ["Ufa", "Lenin str", 1]
#             }
#     }
# print(per["user_1"]["adres"][1])

# for key, val in per.items():
#     print(key, val)

 # Часть 11. Множества.
 # теже списки, только все элементы идут в случайном порядке
 # Элементы не повторяются
 # записываются в фигурных скобок, но в отличии от словарей не имеют  формы "ключ:значение"
 # для получения определенных данных, и удаления всех повторяющихся элементов

# либо
i = set('ghhyy')
print(i)
i = {1,3,3,4,5,7,8,2,6}
print(i)

#работа с множествами такаяже, как и работа со списками
#но мы не можем обращаться к элементу по инденксу и не можем его поменять через [], но можно иначе

i = {1,3,3,4,5,7,8,2,6}
i.add(13) # добавить элемент
print(i)

i = {1,3,3,4,5,7,8,2,6}
i.update([13, 'Hi', True]) # добавить элемент списком
print(i)

i = {1,3,3,4,5,7,8,2,6}
i.remove(6) # удалить элемент
print(i)

i = {1,3,3,4,5,7,8,2,6}
i.pop() # удалить первый элемент
print(i)

i = {1,3,3,4,5,7,8,2,6}
i.clear() #очистить все множество
print(i)

i = [1,3,3,4,5,7,8,2,6]
print (set(i))
# либо

i = [1,3,3,4,5,7,8,2,6]
h = set(i)
print (h)

# frozenset - замороженное множество
# объединение кортежа и множества
# создаем обычное мгножество, но не можем менять элементы внутри множества

i = [1, 3, 3, 4, 5, 7, 8, 2, 6, 13, 'Hi', False, "Hi"]
y = frozenset(i)
print(y)



ЧАсть 12.
















































































































# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
