def func2(l):
    return l[1] + l[2]
def func1(x,y):
    try:
        print(func2([x,y]))
    except:
        print('exception on occurred')
try:
    func1(1)
except:
    print('ok')
print('end')