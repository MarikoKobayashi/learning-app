def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("自然数を入力する："))

