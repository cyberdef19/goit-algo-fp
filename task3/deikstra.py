import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('E', 3)],
    'D': [('B', 7), ('E', 2), ('F', 1)],
    'E': [('C', 3), ('D', 2), ('F', 5)],
    'F': [('D', 1), ('E', 5)]
}

def shortest_path_deikstra(start_vertex: str, graph: dict):

    if start_vertex not in graph.keys():
        print("Такої вершини у графі не існує")
        return

    #Ініціалізуємо асоціативний масив початковими значеннями в нескінченність та стартову вершину в 0
    distances = {vertex: float('infinity') for vertex in graph if vertex != start_vertex}
    distances[start_vertex] = 0

    #Знаходимося у стартовій вершині, тому відстань до нас 0
    heap =[(0, start_vertex)]

    #Доки не обідемо увесь heap
    while heap:
        #Отримуємо мінімальну поточну вагу та ноду графа із усіх вершин
        current_distance, node = heapq.heappop(heap)

        #Якщо поточна відстань гірша за ту, що вже є у масиві вершин, то просто продовжуємо цикл
        if current_distance > distances[node]:
            continue

        #Перебираємо сусідів поточної вершини-ноди і додаємо
        #до відстані, що вже маємо
        for neighbor, weight in graph[node]:
            distance = current_distance + weight

            #Якщо отримана відстань краща, то оновлюємо записи у кучі та в масиві
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

shortest_path_deikstra("A", graph)












