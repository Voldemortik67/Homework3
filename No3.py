def analyze_scores(*scores):# *scores собирает любое количество баллов в кортеж
    count = len(scores)

    if count == 0:# если баллов нет, возвращаем нули (чтобы не делить на ноль)
        return 0, 0, 0

    total = sum(scores)
    average = total / count
    return total, count, average

def print_report(team_name, **info):# **info собирает все именованные аргументы в словарь 
    print("Команда:", team_name)
    for key, value in info.items():
        print(key + ":", value)

total, count, average = analyze_scores(8, 10, 7, 9)
print("Баллы: 8, 10, 7, 9")
print("Сумма:", total, "Количество:", count, "Среднее:", average)

print()

total, count, average = analyze_scores(5, 5)
print("Баллы: 5, 5")
print("Сумма:", total, "Количество:", count, "Среднее:", average)

print()

total, count, average = analyze_scores()
print("Без баллов")
print("Сумма:", total, "Количество:", count, "Среднее:", average)

print()

print_report("Комета", coach="Бурмалдот", city="Йошкар-Ола")