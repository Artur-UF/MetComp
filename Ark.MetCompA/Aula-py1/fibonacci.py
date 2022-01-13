# os primeiros 20 números de Fibonacci
a = 0
b = 1
c = a + b
print(a)
print(b)
print(c)
for n in range(17):
    a = b
    b = c
    c = a + b
    print(c)
