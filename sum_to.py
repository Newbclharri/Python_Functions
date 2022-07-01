def sum_to(num):
    int = 0
    sum = 0
    for i in range(num):
        int = num - i
        sum += int
    return sum

print(sum_to(6))
print(sum_to(10))