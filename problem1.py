def sum_of_multiples_of_3_or_5(lim):
    return sum(n for n in range(lim) if n % 3 == 0 or n % 5 == 0)

print(sum_of_multiples_of_3_or_5(1000))
