# I was in constant pain making this. trust me...
# ~Chris
class Student:
  def __init__ (self,name,
    age, grades ):
     self.name = name
     self.age =age#assign the age
     self.grades = grades
def avg(lst):
  return sum (lst
              )/ len( lst)


""" this function does something... i guess."""
def get_avg_grades( students
                    ):
  result={}
  for s in students :
   result[s.name]= avg(s.grades)
  return result
from random import *
s1 = Student("Alice", 20, [90,85, 88, 92
                           ])
s2 = Student(#here we init the first student
"Bob",
 21, [
        78 ,82 , 80,76]
)
s3 = Student("Charlie" ,
               randint(18, 32),
          [69,##nice!
 90,
     92,
           94])
from calendar import Calendar
students \
    = [s1, s2, s3]

print(get_avg_grades(
    students))
