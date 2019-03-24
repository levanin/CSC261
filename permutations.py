def dfs_backtrack(candidate, input, output):
    if is_solution(candidate, input):
        add_to_output(tuple(candidate), output)
    else:
        for child_candidate in children(candidate, input):
            dfs_backtrack(child_candidate, input, output)


def is_solution(candidate, s):
    return (set(candidate) == s)


def children(candidate, input):
    if len(candidate)== 0:
        return [(a,) for a in input]
    return [candidate + (b,) for b in input.difference(set(candidate))]


def add_to_output(candidate, output):
    output.append(candidate)

def permutations(s):
    solutions = []
    dfs_backtrack("", s, solutions)
    return solutions

print(sorted(permutations({'a'})))