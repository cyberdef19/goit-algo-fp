import uuid

import networkx as nx
import matplotlib.pyplot as plt
from typing import Callable
from random import randint
from matplotlib.animation import FuncAnimation
from collections import deque


class Node:
    def __init__(self, key, color="skyblue", color_walk="brown"):
        self.left = None
        self.right = None
        self.parent = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.color_walk = color_walk
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def random_dark_color():
    r = randint(0, 100)
    b = randint(0, 100)
    g = randint(0, 100)
    return f"#{r:02x}{b:02x}{g:02x}"

def bfs_walk(root: Node) -> list:
    q = deque([root])
    bfs_list = []
    while q:
        node = q.popleft()
        bfs_list.append(node.id)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return bfs_list


def dfs_walk(root: Node) -> list:
    stack = [root]
    dfs_list = []
    while stack:
        node = stack.pop()
        dfs_list.append(node.id)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return dfs_list


def heap_insert(node: Node, root: Node):
    if root is None:
        root = node
        return root

    # Ведемо пошук вшир BFS та знаходимо місце, де вставити ноду
    q = deque([root])
    while q:
        nodeq = q.popleft()
        if nodeq.left is None:
            nodeq.left = node
            node.parent = nodeq
            break
        elif nodeq.right is None:
            nodeq.right = node
            node.parent = nodeq
            break
        else:
            q.append(nodeq.left)
            q.append(nodeq.right)
    temp = node
    while temp.val < temp.parent.val and temp.parent:
        key = temp.parent.val
        temp.parent.val = temp.val
        temp.val = key


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color_walk=node.color_walk, color=node.color,
                       label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
        return graph


def draw_tree(tree_root, tree: nx.DiGraph):
    # tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)
# Створення дерева
root = Node(0, color_walk=random_dark_color())
heap_insert(root, None)
node1 = Node(4, color_walk=random_dark_color())
heap_insert(node1, root)
node2 = Node(5, color_walk=random_dark_color())
heap_insert(node2, root)
node3 = Node(10, color_walk=random_dark_color())
heap_insert(node3, root)
node4 = Node(1, color_walk=random_dark_color())
heap_insert(node4, root)
node5 = Node(3, color_walk=random_dark_color())
heap_insert(node5, root)
node6 = Node(14, color_walk=random_dark_color())
heap_insert(node6, root)
node7 = Node(15, color_walk=random_dark_color())
heap_insert(node7, root)
node8 = Node(100, color_walk=random_dark_color())
heap_insert(node8, root)
node9 = Node(11, color_walk=random_dark_color())
heap_insert(node9, root)
node10 = Node(30, color_walk=random_dark_color())
heap_insert(node10, root)

# Відображення дерева
tree = nx.DiGraph()
draw_tree(root, tree)


def walk_visual(tree: nx.DiGraph, root: Node, func: Callable[[Node], list]):
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    order = func(root)
    fig, ax = plt.subplots(figsize=(9, 6))

    labels = {node[0]: node[1].get('label', node[0]) for node in tree.nodes(data=True)}

    ax.set_axis_off()

    def update(frame):
        ax.clear()
        visited = order[:frame + 1]
        colors = [tree.nodes[n]['color_walk'] for n in visited]
        nx.draw(tree, pos, labels=labels, node_color="blue", arrows=False, node_size=2500, ax=ax)
        nx.draw_networkx_nodes(tree, pos, nodelist=order[:frame + 1], node_size=2500, node_color=colors, ax=ax)

    animate = FuncAnimation(fig, update, frames=len(order), interval=800, repeat=False, blit=False)
    if func.__name__ == "bfs_walk":
        animate.save("bfs.gif", writer="pillow", fps=2)
    if func.__name__ == "dfs_walk":
        animate.save("dfs.gif", writer="pillow", fps=2)
    return animate

walk_visual(tree, root, bfs_walk)
walk_visual(tree, root, dfs_walk)






