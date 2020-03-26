sample = "5 3"

with open('../datasets/rosalind_fib.txt', 'r') as file:
    sample = file.read()

n = int(sample.split()[0])
k = int(sample.split()[1])


def fibonacci(n: int, k: int) -> int:
    a = 0
    b = 1

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b * k
            b = c
        return b


print(fibonacci(n, k))
