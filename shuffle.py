import copy
def shuffle(a,b):
    if len(a) == 0:
        return [b]
    if len(b) == 0:
        return [a]
    x = shuffle(a[1:],b)
    y = shuffle(a,b[1:])
    one = [a[0] + d for d in x]
    two = [b[0] + c for c in y]
    return set(one + two)

def shuffle_language(A, B):
    result = []
    for a in A:
        for b in B:
            c = shuffle(a, b)
            result = result + list(shuffle(a,b))
    return set(result)

print(sorted(shuffle_language({'ab'}, {'cd', 'e'})))

