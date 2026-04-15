# I was in (less) constant pain making this. trust me...
# ~Chris

from random import *

# TODO: typing bekommt ihr selbst hin :)
class Student:
    def __init__(self,
            name,
            age,
            grades):
        self.name = name
        self.age = age  # assign the age
        self.grades = grades


def avg(lst):
    return sum(lst) / len(lst)


def get_avg_grades(students):
    """ SOME USEFUL DESC HERE """
    result = {}
    for s in students:
        result[s.name] = avg(s.grades)
    return result


if __name__ == '__main__':
    s1 = Student("Alice", 20, [90, 85, 88, 92])

    s2 = Student("Bob",21, [78, 82, 80, 76])   # here we init the second student
    s3 = Student("Charlie",
                 randint(18, 32),
                 [69,  ##nice!
                  90,
                  92,
                  94])

    students = [s1, s2, s3]

    print(get_avg_grades(students))
