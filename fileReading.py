import pickle
with open("Student_file.pkl","rb") as file:
    data = pickle.load(file)

for ele in data:
    print(ele.display())