def fibonaci_gen(limit):
    a, b = 0, 1
    for i in range(limit):
        yield b
        a, b = b, a + b

print([value for value in fibonaci_gen(10)])
