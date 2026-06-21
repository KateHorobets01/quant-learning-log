# day1_returns.py

# Цены закрытия акции за 10 дней
prices = [150.0, 152.3, 151.8, 154.0, 153.5, 156.2, 155.0, 157.8, 159.1, 158.4]

# ЗАДАНИЕ 1: индексация
# Сохрани в переменную first_price первую цену из списка
first_price = prices[0]  # замени None на свой код

# Сохрани в переменную last_price последнюю цену из списка
# подсказка: можно использовать индекс -1
last_price = prices[-1]

# ЗАДАНИЕ 2: срезы (slicing)
# Сохрани в переменную first_three первые 3 цены из списка
first_three = prices[:3]

# Сохрани в переменную last_three последние 3 цены из списка
last_three = prices[-3:]

# ЗАДАНИЕ 3: расчёт общей доходности за весь период
# формула: (last_price - first_price) / first_price
total_return = (prices[-1] - prices[0])/prices[0]

# ЗАДАНИЕ 4: посчитай доходность за каждый отдельный день вручную
# (да, это будет выглядеть однообразно — про это ниже)
return_day2 = (prices[1]-prices[0])/prices [0]  # (prices[1] - prices[0]) / prices[0]
return_day3 = (prices[2]-prices[1])/prices [1]   # (prices[2] - prices[1]) / prices[1]
return_day4 = (prices[3]-prices[2])/prices [2]   # (prices[3] - prices[2]) / prices[2]     
# ЗАДАНИЕ 5: собери эти три значения в список с помощью .append()
daily_returns = []
daily_returns.append (return_day2)
daily_returns.append (return_day3)
daily_returns.append (return_day4)
# добавь return_day2, return_day3, return_day4 в daily_returns

# Вывод
print("Первая цена:", first_price)
print("Последняя цена:", last_price)
print("Первые три цены:", first_three)
print("Последние три цены:", last_three)
print("Общая доходность за период:", total_return)
print("Доходности по дням:", daily_returns)