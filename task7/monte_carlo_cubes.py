from random import randint
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

theoretical = {"2":2.78,
"3":5.56,
"4":8.33,
"5":11.11,
"6":13.89,
"7":16.67,
"8":13.89,
"9":11.11,
"10":8.33,
"11":5.56,
"12":2.78
}
def random_cube_digit():
    return randint(1, 6)

def monte_carlo_cubes_sum(num_experiments: int, amount: int) ->list:
    result =[]

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
        result.append({
            "Кількість кидків": amount,
            "Результати": sums_result
        })
        print(f"Експеримент {experiment}")
        print(f"Кількість визначених кидків {amount}")
        print(f"Маємо такі результати сум:")
        print(sums_result)
    return result



amounts = [1000, 10000, 100000, 1000000]
result = []
for amount in amounts:
    result.append(monte_carlo_cubes_sum(5, amount))


def results_to_DataFrame(result: list) -> pd.DataFrame:
    result_to_df = []
    for val in result:
        for v in val:
            for key_sum, item_sum in v["Результати"].items():
                exper = {
                    "Кількість кидків": str(v["Кількість кидків"]),
                    "Сума": int(key_sum),
                    "Результат": item_sum
                }
                result_to_df.append(exper)
    for k, val in theoretical.items():
        theoretical_exper = {
            "Кількість кидків": "Теоретично",
            "Сума": int(k),
            "Результат":val
        }
        result_to_df.append(theoretical_exper)
    result_df = pd.DataFrame(result_to_df)
    return result_df

df = results_to_DataFrame(result)
df_data = df.pivot_table(aggfunc=np.mean, index="Сума", values="Результат", columns="Кількість кидків")

plt.figure(figsize=(8, 6))
sn.heatmap(df_data, annot=True, fmt=".2f", cmap="YlGnBu")
plt.title("Теплова карта ймовірностей рандомних кидків двох кубиків")
plt.ylabel("Сума кубиків")
plt.xlabel("Кількість кидків")
plt.show()