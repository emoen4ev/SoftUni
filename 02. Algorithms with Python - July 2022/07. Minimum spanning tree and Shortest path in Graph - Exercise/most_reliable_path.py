from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' ')]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

start_node = int(input())
end_node = int(input())

pq = PriorityQueue()
pq.put((-100, start_node))

distance = [float('-inf')] * nodes
distance[start_node] = 100

parent = [None] * nodes

while not pq.empty():
    max_distance, node = pq.get()
    if node == end_node:
        break
    for edge in graph[node]:
        child = edge.second if edge.first == node else edge.first
        new_distance = -max_distance * edge.weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))

print(f'Most reliable path reliability: {distance[end_node]:.2f}%')

path = deque()
node = end_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=' -> ')

# ------------- tests --------------

# 7
# 10
# 0 3 85
# 0 4 88
# 3 1 95
# 3 5 98
# 4 5 99
# 4 2 14
# 5 1 5
# 5 6 90
# 1 6 100
# 2 6 95
# 0
# 6

# 4
# 4
# 0 1 94
# 0 2 97
# 2 3 99
# 1 3 98
# 0
# 1

# --------- results ----------

# Most reliable path reliability: 81.11%
# 0 -> 4 -> 5 -> 3 -> 1 -> 6

# Most reliable path reliability: 94.11%
# 0 -> 2 -> 3 -> 1