from student import Student
import os
import pickle

database = "Student_file.pkl"
def save_record(s):
    students_obj_list = []
    students_obj_list.append(s)
    with open(database , "wb") as file:
        pickle.dump(students_obj_list,file)

s1 =Student("Laxya",32,12)
s2 =Student("kolly",31,11)
save_record(s1)
save_record(s2)