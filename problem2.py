def fibonnaci() -> int:
    c, a, b = 0, 0, 1
    total = 0
    while c <= 4000000:
        if c % 2 == 0:
            total += c
        c = a + b
        a, b = b, c
    return total        


def mathematical_fibonacci() -> int:
    c, a, b = 0, 0, 2
    total = 0
    while c <= 4000000:
        total += b
        c = 4 * b + a
        a, b = b, c
    return total


result_fibonnaci = fibonnaci()
print(result_fibonnaci)

result_fibonnaci = mathematical_fibonacci()
print(result_fibonnaci)
