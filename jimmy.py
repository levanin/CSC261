def shuffle(s,t):
    if s == '':
        return [t]
    if t == '':
        return [s]
    result2 = shuffle(s[1:],t)
    result = shuffle(s,t[1:])

    one = [t[0] + d for d in result]
    two = [s[0] + c for c in result2]
    return set(one + two)


print(sorted(shuffle('abab', 'baba')))