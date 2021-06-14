def func(a = 0 , **kwargs):
    print('a:', a)
    print('kwargs:', kwargs)

func(1)
func(a = 1, b=2, c= 3)
