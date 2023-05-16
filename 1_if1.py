"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""



def main(age):
    if age < 6:
        result = 'Вы ходите в детский сад'
    elif 6 <= age <= 17:
        result = 'Вы учитесь в школе'
    elif 18 <= age <= 24:
        result = 'Вы учитесь в ВУЗЕ'
    elif age > 24:
        result = 'Вы ходите на работу'
    else:
        result = 'Что-то пошло не так. Пожалуйста, обратитесь к администратору!'
    return result

age_str = input("Введите ваш возраст: ")
age =int(age_str)
print(age)
    

#print(main(age)) 
#означает, что main будет работать, если вызвали python bot.py,  а если для импорта, то работать не будет
if __name__ == "__main__":
    print(main(age)) 
