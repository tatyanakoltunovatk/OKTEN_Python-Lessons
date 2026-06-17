# Створіть словник з назвою fruit_stock.
# Додайте до нього три пари "ключ: значення":
# "apple": 10
# "banana": 15
# "orange": 8
# Виведіть на екран весь словник fruit_stock.
# Виведіть на екран кількість яблук, звернувшись до значення за ключем "apple".
# Додайте новий фрукт до словника: "груша" зі значенням 12.
# Змініть кількість banana: встановіть нове значення 20.
# Виведіть на екран оновлений словник fruit_stock.

# Option 1:
# fruit_stock= {"apple": 10, "banana": 15,"orange": 8}
# Option 2:
fruit_stock = dict(apple = 10, banana = 15, orange = 8)

print(f"\nPrinting dict fruit_stock: {fruit_stock}")

# Print option 1:
# print("There are", fruit_stock['apple'], "apples in the stock")
# Print option 2:
print(f"There are {fruit_stock['apple']} apples in the stock")

fruit_stock['pear'] = 12
print(f"Pear's added to the fruit_stock. Now the fruit_stock is {fruit_stock}")
fruit_stock['banana'] = 20
print(f"Changed quantity of bananas for {fruit_stock['banana']}. Now the fruit_stock is {fruit_stock}.\n")

# Створення та доступ до елементів списку
#
# Створіть список з назвою shopping_list, який містить наступні рядки: "молоко", "хліб", "яйця", "сир".
# Виведіть на екран весь список.
# Виведіть на екран перший елемент списку (той, що має індекс 0)

shopping_list = ["milk", "bread", "eggs", "cheese"]
print(f"The shopping list is: {shopping_list}")
print(f"The first element of our shopping list is {shopping_list[0]}")
print(f"Last element of the list is {shopping_list[-1]}\n")

# Створи список із 7 собак.
# Кожна собака — словник з трьома полями: "name" (кличка), "age" (вік), "breed" (порода).
# Виведи третю собаку зі списку та її кличку.

dogs = [
    {"name": "Рекс", "age": 5, "breed": "Лабрадор"},
    {"name": "Бім", "age": 3, "breed": "Хаскі"},
    {"name": "Тузик", "age": 4, "breed": "Вівчарка"},
    {"name": "Барні", "age": 2, "breed": "Мопс"},
    {"name": "Чарлі", "age": 6, "breed": "Бульдог"},
    {"name": "Лакі", "age": 1, "breed": "Коргі"},
    {"name": "Макс", "age": 7, "breed": "Доберман"}
]
print(f"The third dog is {dogs[2]}")
print(f"The third dog's name is {dogs[2]['name']}")