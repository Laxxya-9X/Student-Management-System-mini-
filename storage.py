import os
import pickle

DB = "Student_file.pkl"

def load_all():
    if os.path.exists(DB) and os.path.getsize(DB) > 0:
        with open(DB, "rb") as f:
            return pickle.load(f)
    return []

def save_all(students):
    with open(DB, "wb") as f:
        pickle.dump(students, f)

def add(student):
    students = load_all()
    if any(babu.roll_no == student.roll_no for babu in students):
        return False                      # babu to phle se hi hai chalo wps  hahaha
    students.append(student)  # jab babu db me nhi mile to append krna hai
    save_all(students)
    return True 

def find(roll_no):
    return next((babu for babu in load_all() if babu.roll_no == roll_no), None) # babu ko roll no se list dundh rhe hai 

def update(roll_no, name=None, grade=None):
    students = load_all()
    for babu in students:
        if babu.roll_no == roll_no:
            if name: babu.name = name
            if grade: babu.grade =grade
            save_all(students)
            return True
    return False

def delete(roll_no):
    students = load_all()
    remaining = [babu for babu in students if babu.roll_no != roll_no]
    if len(remaining) == len(students):
        return False
    save_all(remaining)
    return True