class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def __str__(self):
        return f"Name : {self.name} | Roll : {self.roll_no}| Grade : {self.grade}"