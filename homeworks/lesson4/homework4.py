# Вивести кожне число зі списку

numbers = [1, 2, 3, 4, 5]

print(f"\nThe quantity of numbers in the list is {len(numbers)}")

index = 0
# Option 1:
for item in numbers:
    if index == 0:
        print("--- \nStarting for loop...")
    print(f"element with index #{index} is {item}")
    if index == len(numbers)-1:
        print(f"--- \nFor loop ended. Last index is #{index}\n")
    index = index + 1


count = 0
# Option 2:
while count < len(numbers):
    if count == 0:
        print(f"--- \nStarting while loop...")
    print(f"While loop: element with index #{count} is {numbers[count]}")
    if count == len(numbers)-1:
        print(f"--- \nWhile loop ended. Last index is #{count}\n")
    count += 1

print('-------------')

# Створи масив із 10 будь-яких чисел. За допомогою циклу підрахуй, скільки серед них парних чисел.
arrNumbers = [27, 56, 12, 2, 88, 67, 10, 8, 11, 55, 0, -12]
counter = 0
for num in arrNumbers:
    if num % 2 == 0:
        counter = counter + 1
print(f"There are {counter} even numbers in the list")
print('-------------')

# Створи масив із 5 чисел. За допомогою циклу порахуй суму всіх чисел у цьому масиві.
my_list = [45, 8, 7, 48, 13, 25, -100]
total = 0

for num in my_list:
    total = total + num

print(f"The total is {total}")
print('-------------')

# Є об’єкт (словник), у якому зберігаються імена студентів та їхніх пропусків.
# За допомогою циклу виведи на екран усіх студентів у такому форматі:
# Ім'я: Петро, Пропусків: 18

students = {
    'Олег': 5,
    'Катерина': 3,
    'Іванка': 6,
    'Ілона': 0,
    'Максим':5
}

for student in students:
    print(f"Ім'я: {student}, Пропусків: {students[student]}")




