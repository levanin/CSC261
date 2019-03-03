def all_strings(alpha, length):
    if length == 0:
        return ['']
    if length == 1:
        return alpha
    else:
        star = all_strings(alpha, length - 1)
        result = []
        for a in star:  # remember this handy thing
            for b in alpha:  # this is handy af
                result += [str(a) + str(b)]
        return result


print(sorted(all_strings({0, 1}, 0)))
