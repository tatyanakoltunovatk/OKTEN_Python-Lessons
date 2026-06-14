# Створіть дві змінні, is_sunny (чи сонячно) та is_warm (чи тепло), і присвойте їм булеві значення (True або False).
# Перевірте, чи можна йти гуляти (умова: сонячно і тепло). Виведіть результат.
# Перевірте, чи можна вдягнути футболку (умова: сонячно або тепло). Виведіть результат.

## Перевірте, чи можна йти гуляти (умова: сонячно і тепло). Виведіть результат.
print("** TASK 1 **")
is_sunny = True
is_warm = False

if is_sunny and is_warm:
    print('You may go for a walk')
else:
    print("You'd better stay in today.")

## Перевірте, чи можна вдягнути футболку (умова: сонячно або тепло). Виведіть результат.
if is_sunny or is_warm:
    if is_sunny:
        print("You can wear a t-shirt. It's sunny.")
    elif is_warm:
        print("You can wear a t-shirt. It's warm.")
else:
    print("You'd rather search for something else to wear than a t-shirt")

# Маємо змінні day яка символізує назву дня тижня (наприклад, "Понеділок", "Субота")
# і за допомогою конструкції match визначає, чи є цей день робочим, вихідним, чи невірною назвою.
# Визначає тип дня тижня (робочий/вихідний) за його назвою.

print("\n** TASK 2 **")
day = 'Friday'

match day:
    case 'Monday':
        print(f'{day} is a working day')
    case 'Tuesday':
        print(f'{day} is a working day')
    case 'Wednesday':
        print(f'{day} is a working day')
    case 'Thursday':
        print(f"{day} is a working day, but it's almost Friday")
    case 'Friday':
        print(f'{day} is a working day. Happy {day}!')
    case 'Saturday':
        print(f"Weekend has started! It's {day}")
    case 'Sunday':
        print(f"{day} is a weekend. Be careful, tomorrow's Monday")
    case _:
        print('Invalid day name')