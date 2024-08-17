def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors.append((divisor, count))
        divisor += 1
    return factors

# Example Usage:
number = 60
print(prime_factors(number))  # Output: [(2, 2), (3, 1), (5, 1)]
