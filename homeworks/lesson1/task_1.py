# Створіть 6 змінних з будь-якими значенням

my_var_1_str = 'my_string'
my_var_2_str = "my_string_2"
my_var_3_int = 12
my_var_4_int = 100
my_var_5_float = 3.14
my_var_6_bool = False

# Робота з числами
# Умова:
#
# Створіть дві змінні, a та b, та присвойте їм будь-які числові значення (цілі або дробові).
# Обчисліть їх суму, різницю і тд.
# Виведіть результати кожної операції на екран з відповідними поясненнями.

a = 12
b = 100.1

add = a + b
print(f"{a} plus {b} equals:", add)

deduct = b - a
print(f"{b} minus {a} equals:", deduct)

multiply = a * b
print(f"{a} multiplied by {b} equals:", multiply)

divide = b / a
print(f"{b} divided by {a} equals:", divide)

int_divide = b // a
print(f"integer division: {b} // {a} equals:", int_divide)

mod = b % a
print(f"modulus division: {b} % {a} equals:", mod)

# Робота з рядками (Strings)
# Умова:
#
# Створіть змінну first_name та присвойте їй ваше ім'я.
# Створіть змінну last_name та присвойте їй ваше прізвище.
# Створіть змінну full_name, об'єднавши (конкатенувавши) ім'я та прізвище через пробіл.
# Виведіть full_name на екран.

first_name = "Tetiana"
last_name = "Koltunova"
full_name = first_name + " " + last_name
full_name_2 = f"{first_name} {last_name}"

print(full_name)
print("My full name is", full_name_2)

