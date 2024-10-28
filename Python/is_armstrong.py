def is_armstrong(n):
    power = len(str(n))
    return sum(int(digit) ** power for digit in str(n)) == n
