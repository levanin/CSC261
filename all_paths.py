def dfs_backtrack(candidate, destination, input, output):
    if is_solution(candidate, destination, input):
        add_to_output(candidate, output)
    else:
        for child_candidate in children(candidate, input):
            dfs_backtrack(child_candidate, destination, input, output)


def is_solution(candidate, destination, s):
    return candidate[-1] == destination


def children(candidate, input):
    return [candidate + [b] for b in input[candidate[-1]] if b not in candidate]


def add_to_output(candidate, output):
    output.append(candidate)

def all_paths(graph_string, source, destination):
    solutions = []
    adjlist = adjacency_list_unweighted(graph_string)
    dfs_backtrack([source], destination, adjlist, solutions)
    return solutions


def adjacency_list_unweighted(graph_str):
    lines = str(graph_str).splitlines()
    params = lines[0].split() # array of first line defining the graph's parameters
    isweighted = True if params[0] == "D" else False
    adjlist = [[] for _ in range(int(params[1]))]  # list of empty lists equal to the number of nodes
    for line in lines[1:]:
        numbers = [int(n) for n in line.split()] # transition relation on each line
        has3 = True if len(numbers) == 3 else False
        for i in range(len(adjlist)):

            if isweighted == True:
                if i == numbers[0]:
                    adjlist[i].append(numbers[1])
            else:
                if i == numbers[0]:
                    adjlist[i].append(numbers[1])
                if i == numbers[1]:
                    adjlist[i].append(numbers[0])
    return adjlist

from pprint import pprint

# graph in fig 5.15 of textbook
# vertices 0 to 6 correspond to A to G
graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

pprint(sorted(all_paths(graph_str, 6, 3)))