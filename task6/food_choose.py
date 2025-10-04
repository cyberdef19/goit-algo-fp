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
    pass


print(greedy_algorithm(4000))

