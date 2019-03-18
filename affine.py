def affinef(plaintext, a, b):
    x = list(plaintext)
    for i in range(len(x)):
        if (x[i] != " "):
            t = ord(x[i])-97
            s = x[i]

            x[i] = chr(((a * (ord(x[i]) - 97) + b) % 26) + 97)
            print("f(" + s + ") = " + str(a) + "*" + str(t) + ' + ' + str(b) + "\n= " + str(ord(x[i])-97) + "\n= " + x[i]) # messy printing statement
    return "".join(x)


plain = input("Enter plaintext: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Ciphertext is: " + affinef(plain, a, b))
