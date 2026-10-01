from student import Student
import storage

def menu():
    while True:
        print("\n1.Add  2.View all  3.Search  4.Update  5.Delete  6.Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            try:
                name  = input("Name: ")
                roll  = int(input("Roll no: "))
                grade = int(input("Grade: "))
            except ValueError:
                print("Roll and grade must be numbers."); continue
            print("Added!" if storage.add(Student(name, roll, grade))
                  else "Roll number already exists.")
        elif choice == "2":
            for s in storage.load_all(): print(s)
        elif choice == "3":
            s = storage.find(int(input("Roll no: ")))
            print(s if s else "Not found.")
        elif choice == "4":
            roll = int(input("Roll no: "))
            ok = storage.update(roll, input("New name (blank=skip): "),
                                 None)
            print("Updated." if ok else "Not found.")
        elif choice == "5":
            print("Deleted." if storage.delete(int(input("Roll no: ")))
                  else "Not found.")
        elif choice == "6":
            break

menu()