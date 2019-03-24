def invertibleelements(m):
    elements = set()
    for i in range(m):
        for j in range(m):
            if (i*j) % m == 1:
                elements.add(i)
    return elements

print(invertibleelements(21))