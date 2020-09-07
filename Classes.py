class Student:
    def __init__(self, name, age, course, grade, living_at_university):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
        self.living_at_university = living_at_university

    def whatdegree(self):
        if self.grade >= 70:
            return "1st Class"
        elif self.grade >= 60:
            return "2:1"
        elif self.grade >= 50:
            return "2:2"
        elif self.grade >= 40:
            return "3rd Class"
        else:
            return "fail"

class Graduate(Student):
    def __init__(self, name, age, course, grade, living_at_university, in_a_job ):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
        self.living_at_university = living_at_university
        self.in_a_job = in_a_job