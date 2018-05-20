
class Individual:

    def __init__(self, id, first, last):
        self.id = id
        self.first = first
        self.last = last

    @property
    def name(self):
        return f'{self.first} {self.last}'


class Student(Individual):

    def __init__(self, id, first, last):
        super().__init___(id, first, last)


class Admin(Individual):

    def __init__(self, id, first, last):
        super().__init___(id, first, last)