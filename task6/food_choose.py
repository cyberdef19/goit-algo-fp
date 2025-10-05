import heapq

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(budget: float) -> {}:
    ratio_calories_costs = [(-v["calories"]/v["cost"], k) for k, v in items.items()]
    heapq.heapify(ratio_calories_costs)
    result = {}
    while budget > 0 and len(ratio_calories_costs) > 0:
        val = heapq.heappop(ratio_calories_costs)
        food = val[1]
        item = items[food]
        amount_food = budget//item["cost"]
        if amount_food != 0:
            result[food] = amount_food
        amount_coins = amount_food * item["cost"]
        budget -= amount_coins
    return result



def dynamic_programming(budget: int) -> {}:
    result = {}
    foods = list(items.keys())
    costs = [items[name]["cost"] for name in foods]
    calories = [items[name]["calories"] for name in foods]

    #Створимо список оптимальних страв та максимальних калорій
    #для кожного бюджета від 0 до budget
    set_optimum = [{"foods": [],
                    "calories": 0} for _ in range(budget + 1)]

    for i in range(len(foods)):
        cost, cal = costs[i], calories[i]
        for b in range(cost, budget + 1):
            if set_optimum[b - cost]["calories"] + cal > set_optimum[b]["calories"]:
                set_optimum[b]["calories"] = set_optimum[b - cost]["calories"] + cal
                set_optimum[b]['foods'] = set_optimum[b - cost]['foods'] + [foods[i]]
    set_foods = set()
    #підраховуємо кількість товарів, що потрапили у список їжі
    for val in set_optimum[budget]["foods"]:
        set_foods.add(val)
    while set_foods:
        elem = set_foods.pop()
        count = set_optimum[budget]['foods'].count(elem)
        result[elem] = count
    result["calories"] = set_optimum[budget]["calories"]

    return result


print(dynamic_programming(100))
print(greedy_algorithm(100))








