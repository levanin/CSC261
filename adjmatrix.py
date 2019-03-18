def adjacency_matrix(graph_str):
    lines = str(graph_str).splitlines()
    params = lines[0].split()  # array of first line defining the graph's parameters
    numnodes = int(params[1])
    adjlist = populate(numnodes)
    isdirected = True if params[0] == "D" else False
    for line in lines[1:]:
        numbers = [int(n) for n in line.split()]  # transition relation on each
        weight = numbers[2]
        adjlist[numbers[0]][numbers[1]] = weight
        if isdirected == False:
            adjlist[numbers[1]][numbers[0]] = weight

    return adjlist

def populate(numnodes):
    adjlist = [[float('inf') for _ in range(numnodes)] for _ in
               range(numnodes)]  # matrix of empty lists equal to the number of nodes
    for i in range(numnodes):
        for j in range(numnodes):
            if i == j:
                adjlist[i][j] = 0
    return adjlist

graph_str = """\
D 2 W
0 1 4
"""

print(adjacency_matrix(graph_str))