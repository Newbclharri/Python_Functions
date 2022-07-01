def get_product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(get_product(-1, 4))
print(get_product(2,5,5))
print(get_product(4,0.5,5))