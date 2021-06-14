def func(a, results= None):
    if results is None:
        results =[]
    results.append(a)
    return results

l = func(3)
print(func(1))
print(func(2))
print(l)
