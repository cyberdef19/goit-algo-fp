import networkx as nx
from random import  randint


def create_graph():
    gx = nx.complete_graph(10)
    for u, v in gx.edges():
        gx[u][v]["weight"] = randint(0, 10)
        print(u, v)
    return gx

#Оберемо випадково початкову вершину
start_vert = randint(0, 10)


