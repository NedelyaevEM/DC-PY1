money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital > 0:
    money_capital = money_capital - (spend * (1 + increase) ** month)
    if money_capital > 0:
        money_capital += salary
        month += 1
    else:
        break

print(month)
