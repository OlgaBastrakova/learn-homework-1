"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""
    
def hello_user(): 
    while True: 
        user_say = input('Скажи что-нибудь: ') 
        if user_say == 'Пока': 
            print('Ну пока') 
            break 
        else: 
            print('Сам ты {}'.format(user_say))

if __name__ == "__main__":
    hello_user()
