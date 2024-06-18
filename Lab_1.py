num1 = int(input("Введіть перше ціле число: "))
num2 = int(input("Введіть друге ціле число: "))
num3 = float(input("Введіть перше дробове число: "))
num4 = float(input("Введіть друге дробове число: "))
results = [
   num1 + num2,         
   num1 - num2,       
   num1 * num2,           
   num1 / num2,
    num1 ** num2,            
    num1 // num2,
    num1 % num2
]
print("Результати операцій:", results)
num_elements = len(results)
print("Кількість елементів у списку:", num_elements)
print("Парні елементи у списку:")
for result in results:
    if result % 2 == 0:
        print(result)
if num_elements >= 5:
    results[1], results[4] = results[4], results[1]
print("Список після заміни другого і п'ятого елементів:", results)
name = str(input("Введіть ваше прізвище та ім'я: "))
print("Виконавець лабораторної роботи:"+str(name))
print("Лабораторна робота виконана")
