def fatorial(num , show=False):
    result = 1
    for c in range(num, 0, -1):
        result *= c
        if show == True:
            print(f"{result} * {c}  ->", end=" ")
    return result

s = fatorial(5, show=True)
print(s)