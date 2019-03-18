def adjacency_list(graph_str):
    lines = str(graph_str).splitlines()
    params = lines[0].split() # array of first line defining the graph's parameters
    isweighted = True if params[0] == "D" else False
    adjlist = [[] for _ in range(int(params[1]))]  # list of empty lists equal to the number of nodes
    for line in lines[1:]:
        numbers = [int(n) for n in line.split()] # transition relation on each line
        has3 = True if len(numbers) == 3 else False
        for i in range(len(adjlist)):
            weight = numbers[2] if has3 == True else None
            if isweighted == True:
                if i == numbers[0]:
                    adjlist[i].append((numbers[1], weight))
            else:
                if i == numbers[0]:
                    adjlist[i].append((numbers[1], weight))
                if i == numbers[1]:
                    adjlist[i].append((numbers[0], weight))
    return adjlist
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""
print(adjacency_list(graph_string))