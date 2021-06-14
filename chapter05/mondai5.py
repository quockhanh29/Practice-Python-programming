#(1) 引数を1つ取り、その値の二乗を返す関数squareを定義してください（引数は数値が渡される前提で構いません）
def square(x):
    return x**2
print(square(2))
print(square(3))
#(2) 以下のプログラムが実行できるように関数mulを作成してください。（一つ目の引数は必須です）
def mul(*x):
    m = 1
    for a in x:
        m *=a
    return m
print(mul(1,2))
print(mul(2,4,6))
print(mul(3,5,7,11))
#(3)
def power(x):
    def result(y):
        return y**x
    return result

power3 = power(3)
power4 = power(4)

print(power3(2))
print(power4(3))

#4
s = 0
temp = 0
while True:
    x1 = input('please input number:')
    try:
        temp +=int(x1)
        print(s, ' + ', x1, ' = ', temp)
        s = temp
    except:
        print('not a number is inputted. program exit.')
        break

