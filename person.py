peopleIndex = []

class Person(object):
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

def add_new_person(person: Person):
    peopleIndex.append(person)