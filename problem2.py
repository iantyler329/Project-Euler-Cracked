def sum_even_fibonacci(lim):
    fib1, fib2 = 1, 2
    total_sum = 0
    
    while fib1 <= lim:
        if fib1 % 2 == 0:
            total_sum += fib1
        fib1, fib2 = fib2, fib1 + fib2
    
    return total_sum

print(sum_even_fibonacci(4000000))  # Expected output: 4613732
