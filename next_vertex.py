def next_vertex(in_tree, distance):
    shortest = distance[0]
    for i in range(len(distance)):
        if shortest > distance[i] and in_tree[i] != True:
            shortest = distance[i]
    return distance.index(shortest)

in_tree = [False, True, True, False, False]
distance = [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance))