import random

eq_price = 200
std_dev = 10 # smaller deviation to achieve 0.05 increment or decrement

for i in range(10000):
    price = round(random.normalvariate(eq_price, std_dev) / 0.05) * 0.05 # round to nearest 0.05
    print(round(price, 2))