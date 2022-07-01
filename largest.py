def largest(list):
    return max(list)

def largest2(list):
    max = 0    
    for value in list:
        if value > max:
            max = value
    return max

print(largest([100,20,400,0,5,3]))

print(largest2([1,2,3,37,4]))