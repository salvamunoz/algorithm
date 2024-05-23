# program that will calculate the factorial of a given number

def iterative_factorial(n: int) -> int:
    fact = 1
    for i in range(n):
        fact *= i + 1
    return fact

print(iterative_factorial(5))