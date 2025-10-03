import uuid

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.parent = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())# Унікальний ідентифікатор для кожного вузла

def bfs_walk(root: Node):
    q = deque([root])
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def dfs_walk(root: Node):
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


def heap_insert(node: Node, root: Node):
    if root is None:
        root = node
        return root

    #Ведемо пошук вшир BFS та знаходимо місце, де вставити ноду
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
        graph.add_node(node.id, color=node.color, label=node.val)# Використання id та збереження значення вузла
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}# Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
#root = Node(0)
#root.left = Node(4)
#root.left.left = Node(5)
#root.left.right = Node(10)
#root.right = Node(1)
#root.right.left = Node(3)
# Створення дерева
root = Node(0)
heap_insert(root, None)
node1 = Node(4)
heap_insert(node1, root)
node2 = Node(5)
heap_insert(node2, root)
node3 = Node(10)
heap_insert(node3, root)
node4 = Node(1)
heap_insert(node4, root)
node5 = Node(3)
heap_insert(node5, root)
node6 = Node(14)
heap_insert(node6, root)
node7 = Node(15)
heap_insert(node7, root)
node8 = Node(100)
heap_insert(node8, root)
node9 = Node(11)
heap_insert(node9, root)
node10 = Node(30)
heap_insert(node10, root)

# Відображення дерева
draw_tree(root)
