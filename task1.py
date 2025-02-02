from pulp import *

# Створення задачі
prob = LpProblem("Оптимізація виробництва напоїв", LpMaximize)

# Змінні рішення
lemonade = LpVariable("Кількість лимонаду", 0, None, LpInteger)
juice = LpVariable("Кількість фруктового соку", 0, None, LpInteger)

# Цільова функція
prob += lemonade + juice, "Загальна кількість напоїв"

# Обмеження
prob += 2 * lemonade + juice <= 100, "Обмеження води"
prob += lemonade <= 50, "Обмеження цукру"
prob += lemonade <= 30, "Обмеження лимонного соку"
prob += 2 * juice <= 40, "Обмеження фруктового пюре"

prob.solve()

# Результати
print("Статус:", LpStatus[prob.status])
print("Кількість лимонаду:", lemonade.varValue)
print("Кількість фруктового соку:", juice.varValue)
print("Загальна кількість напоїв:", value(prob.objective))