class Student:
    def __init__(self,Name,RollNo , Std):
        self.Name = Name
        self.RollNo = RollNo
        self.Std = Std

    def display(self):
        return f"Name : {self.Name} , Roll_No. : {self.RollNo} , Class : {self.Std}"

# s1 = Student("Laxya",23,12)
# print(s1)