# program that will calculate the factorial of a given number

def iterative_factorial(n: int) -> int:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def recursive_factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n - 1)
        temp *= n
    return temp

print(iterative_factorial(5))
print(recursive_factorial(5))
