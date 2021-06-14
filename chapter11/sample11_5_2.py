class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.age, self.sex)

    