"""Moss cannot live without his laptop. His laptop cannot live long without its charger. When travelling overseas,
he sometimes needs to use a plug adapter to be able to plug the charger in. Sometimes he even has to create a chain of
these adapters.
For example if his charger plug is of type A and he needs to plug it into a socket of type C, he can use two adapters AB
and BC to plug the charger in. He has a collection of different adapters from previous trips. He wants to get his
charger plugged in with a minimum number of adapters (ideally none).

You have to write a function adapter_chain(adapters_info, charger_plug, wall_socket) that returns the shortest chain of
adapters required in order to connect the charger plug into the wall socket. The details of input and output follow.

Input:
adapters_info is the string representation of a directed graph. The number of vertices is the total number of
plug/socket types in the world. For each plug adapter that Moss owns, there is an edge from the type of socket on the
adapter to the type of plug.
charger_plug is a natural number that specifies the type of plug on the laptop charger.
wall_socket is a number that specifies the type of socket on the wall.

Output:
The function must return a shortest list of types of adapter that, when connected in order (from left to right), the
charger can be connected to the wall socket. The list must always start with the type of plug on the charger and end
with the type of socket on the wall. If it’s not possible to make a connection with (or without) the available adapters,
the function must return the string "CS Unplugged!" (without the quotes)."""


def pre_weighted_adjacency_list(graph_str):
    lines = str(graph_str).splitlines()
    params = lines[0].split()  # array of first line defining the graph's parameters
    isdirected = True if params[0] == "D" else False
    adjlist = [[] for _ in range(int(params[1]))]  # list of empty lists equal to the number of nodes
    for line in lines[1:]:
        numbers = [int(n) for n in line.split()]  # transition relation on each line
        has3 = True if len(numbers) == 3 else False
        for i in range(len(adjlist)):
            weight = numbers[2] if has3 == True else None
            if isdirected == True:
                if i == numbers[0]:
                    adjlist[i].append((numbers[1], 1))
            else:
                if i == numbers[0]:
                    adjlist[i].append((numbers[1], 1))
                if i == numbers[1]:
                    adjlist[i].append((numbers[0], 1))
    return adjlist


def dijkstra(adjlist, start):
    n = len(adjlist)
    intree = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[start] = 0
    for _ in range(n):
        if not all(intree):
            u = next_vertex(intree, distance)
            intree[u] = True
            for v, weight in adjlist[u]:
                if intree[v] is False and (distance[u] + weight) < distance[v]:
                    distance[v] = distance[u] + weight
                    parent[v] = u
    return parent, distance


def next_vertex(in_tree, distance):
    shortest = float('inf')
    location = -1
    for i in range(len(distance)):
        if shortest > distance[i] and in_tree[i] is False:
            shortest = distance[i]
            location = i
    return location


def shortest_path(parent, destination, start=0):
    current = destination
    path = [destination]

    n = len(parent)
    while parent[current] is not None:
        path.insert(0, parent[current])
        current = parent[current]
    return path if path[0] == start else None


def adapter_chain(adapters_info, charger_plug, wall_socket):
    adjlist = pre_weighted_adjacency_list(adapters_info)
    start = charger_plug
    destination = wall_socket
    parent, distance = dijkstra(adjlist, start)
    s = shortest_path(parent, destination, start)
    return "CS Unplugged!" if s is None else s


adapters_info_str = """\
D 5
0 1
0 2
1 2
2 3
1 3
3 0
"""

print(adapter_chain(adapters_info_str, 1, 0))
print(adapter_chain(adapters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
print(adapter_chain(adapters_info_str, 4, 4))
print(adapter_chain(adapters_info_str, 3, 3))
print(adapter_chain(adapters_info_str, 3, 2))
print(adapter_chain(adapters_info_str, 3, 4))
