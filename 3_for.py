"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов

* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

stock =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

for item in stock:
    sum1 = sum(item['items_sold'])
    print(f"Сумма продаж для каждого товара {item['product']}: {sum1}")    
    sum2 = sum(item['items_sold'])/len(item['items_sold'])  
    #a= len(item['items_sold'])
    #print( {a})
    print(f"Cреднее количество продаж для каждого товара {item['product']}: {sum2}")   


total_sales=0
a=0
for item in stock:
    total_sales += sum(item['items_sold'])
    avg = total_sales/len(item['items_sold'])
    a = a + len(item['items_sold'])
    #print({a})


print (f"Сумма продаж всех моделей {total_sales}")
#print (f"Сумма продаж {avg}")
print (f"Cреднее количество продаж всех товаров {total_sales/a}")

