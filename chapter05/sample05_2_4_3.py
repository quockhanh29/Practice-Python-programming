def func(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

func()
func(1,2)
func(a = 3, b=4)
func(1,2,3,c =4, d=3, a=2)
