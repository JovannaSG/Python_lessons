a: int = 123456789
sum: int = 0
while a % 10 != 0:
    sum += a % 10
    a //= 10
    print(a)
print(sum)
