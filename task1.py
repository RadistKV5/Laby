money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 0 # TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
a = money_capital + salary - spend
while a > 0:
    spend *= 1.05
    a = a + salary - spend
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)