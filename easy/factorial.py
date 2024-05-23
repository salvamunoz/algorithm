# program that will calculate the factorial of a given number

def iterative_factorial(n: int) -> int:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

print(iterative_factorial(5))