def average_grade(a, b, c):
    # считаем среднее арифметическое и возвращаем его
    return (a + b + c) / 3

def grade_message(average):
    # выбираем сообщение по среднему баллу
    if average >= 4.5:
        return "Отлично"
    elif average >= 3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"

# Первый набор оценок
avg1 = average_grade(5, 4, 5)
print("Оценки: 5, 4, 5")
print("Средний балл:", round(avg1, 2))
print("Сообщение:", grade_message(avg1))

print()

# Второй набор оценок (функции не меняем, просто вызываем снова)
avg2 = average_grade(3, 4, 3)
print("Оценки: 3, 4, 3")
print("Средний балл:", round(avg2, 2))
print("Сообщение:", grade_message(avg2))