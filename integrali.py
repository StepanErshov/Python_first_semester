import math

def f(u):
    return math.exp(u) / (math.exp(3*u/2) * math.sqrt(u))

# Находим значение интеграла методом Симпсона
# с точностью до 10^-6
def simpson_rule(a, b):
    n = 50   # число разбиений
    h = (b - a) / n   # шаг
    x = [a + i*h for i in range(n+1)]   # узлы
    y = [f(x[i]) for i in range(n+1)]   # значения функции в узлах
    s1 = sum(y[1:n:2])   # значение интеграла на нечетных узлах
    s2 = sum(y[2:n:2])   # значение интеграла на четных узлах
    return (h/3) * (y[0] + y[n] + 4*s1 + 2*s2)

# Находим значение несобственного интеграла
# с помощью замены переменных
def improper_integral():
    a = 0
    b = math.log(2)
    return simpson_rule(a, b)

# Выводим результат
print(improper_integral())