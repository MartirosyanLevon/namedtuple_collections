from collections import namedtuple

Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'yellow')
print(tom)
print(tom[2])
print(tom.age)

Employee = namedtuple('Employee', ['id', 'name'])
w = Employee(1, "Smith")
print(w)
print(w.name)
