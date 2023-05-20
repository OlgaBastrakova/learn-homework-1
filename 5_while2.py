"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

knowledge_base = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'Как тебя зовут?': 'Меня зовут Алиса'
}

def get_answer(question, knowledge_base):
    if question in knowledge_base:
        return knowledge_base[question]
    else:
        return 'Я не знаю ответ на этот вопрос'

       

while True:
    user_question = input('Задайте свой вопрос: ')
    answer = get_answer(user_question, knowledge_base)
    print(answer)
    if KeyboardInterrupt:
        break

if __name__ == "__main__":
    get_answer()
