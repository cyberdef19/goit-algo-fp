from random import randint
from tabulate import tabulate
import pandas as pd

def random_cube_digit():
    return randint(1, 6)

def monte_carlo_cubes_sum(num_experiments: int, amount: int):
    result ={}

    #Кількість експериментів

    for experiment in range(num_experiments):
        sums = {'' + str(x): 0 for x in range(2, 13)}
        #Кількість вкидань кубиків
        for _ in range(amount):
            cube1_digit = random_cube_digit()
            cube2_digit = random_cube_digit()

            sum_cubes = cube2_digit + cube1_digit
            sums[str(sum_cubes)] += 1
        sums_result = {k: (v / amount) * 100 for k, v in sums.items()}
        result[str(experiment)] = {
            "Кількість кидків": amount,
            "Результати": sums_result
        }
        print(f"Експеримент {experiment}")
        print(f"Кількість визначених кидків {amount}")
        print(f"Маємо такі результати сум:")
        print(sums_result)
    return result



amounts = [1000, 10000, 100000, 1000000]
result = []
for amount in amounts:
    result.append(monte_carlo_cubes_sum(5, amount))

for value in result:
    for key, val in value.items():
        table = tabulate(

            headers=,
            tablefmt='grid',
        ).splitlines()


