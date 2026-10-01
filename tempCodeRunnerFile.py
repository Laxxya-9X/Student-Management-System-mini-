from student import Student
import os
import pickle

database = "Student_file.pkl"
student_obj_list = []
def save_record(s):
    if os.path.exists(database) and os.path.getsize(database)> 0:
        with open(database , "rb+") as file:
            data =  pickle.load(file)
            student_obj_list