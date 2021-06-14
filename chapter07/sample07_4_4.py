class Duck:
    def cry(self):
        return 'quack'
class cat:
    def cry(self):
        return 'quack'
def duck_check(something):
    if something.cry() == 'quack':
        print('something is duck')
duck_check(Duck())
duck_check(cat())
