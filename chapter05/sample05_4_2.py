def adder(a):
    def inner(x):
        return x + a
    return inner

add3 = adder(3)
add5 = adder(5)

print(add3(10))
print(add5(10))

