def ticket_total(count, price=12):
    return count * price

def final_price(count, is_school_group=False):
    total = ticket_total(count)#используем уже готовую функцию ticket_total
    if is_school_group:
        total = total * 0.75#скидка 25%, значит платим 75% от суммы
    return total

print("3 обычных билета:", final_price(3), "руб.")# 1) 3 обычных билета (цена по умолчанию)

print("4 билета для школьной группы:", final_price(4, is_school_group=True), "руб.")# 2) 4 билета для школьной группы (именованный аргумент)

print("2 билета по 15 руб.:", ticket_total(2, price=15), "руб.")# 3) 2 билета по 15 рублей (цену передаём сами)

print()
print("2 билета с ценой по умолчанию:", ticket_total(2), "руб.")# Разница между значением по умолчанию и переданным значением
print("2 билета с ценой 15 руб.:", ticket_total(2, price=15), "руб.")