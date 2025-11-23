class Student:
    def __init__(self, name, phone, age, email, group=None):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email
        self.group = group

    def update(self):
        while True:
            kod=input(" What do you want to update?\n 1. Name\n 2. Phone\n 3. Age\n 4. Email\n 5. Exit\n ")
            if kod == "1":
                self.name = input("Enter new name:\n ")
            elif kod == "2":
                self.phone = input("Enter new phone:\n ")
            elif kod == "3":
                self.age = input("Enter new age:\n ")
            elif kod == "4":
                self.email = input("Enter new email:\n ")
            elif kod == "5":
                break
            else:
                print("Invalid input")

class Group:
    def __init__(self, title, direction):
        self.title = title
        self.direction = direction
        self.students = []

    def add_student(self):
        name = input(" Enter name of the student:\n ")
        phone = input(" Enter phone number of the student:\n ")
        age = input(" Enter age of the student:\n ")
        email = input(" Enter email of the student:\n ")
        student = Student(name, phone, age, email)
        self.students.append(student)

    def view_students(self):
        count = 0
        for item in self.students:
            count+=1
            print(f'{count}. Name:{item.name}, Phone:{item.phone}, Age:{item.age}, Email:{item.email}')

    def update_students(self):
        print(" Choose a student to update:\n")
        self.view_students()
        kod=int(input(" Enter student number:\n "))
        if 1<=kod<=len(self.students):
            self.students[kod-1].update()
        else:
            print("Invalid student number")
            return

    def delete_student(self):
        print(" Choose a student to delete:\n")
        self.view_students()
        kod=int(input(" Enter student number:\n "))
        if 1<=kod<=len(self.students):
            self.students.pop(kod-1)
        else:
            print("Invalid student number")
            return

    def update_group(self):
        while True:
            kod=int(input(" What do you want to update?\n 1. Title\n 2. Direction\n 3. Exit\n "))
            if kod == "1":
                self.title = input("Enter new title:\n ")
            elif kod == "2":
                self.direction = input("Enter new direction:\n ")
            elif kod == "3":
                break
            else:
                print("Invalid input")

class Uni:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input(" Enter group title:\n ")
        direction = input(" Enter direction of the group:\n ")
        group = Group(title,direction)
        self.groups.append(group)

    def view_groups(self):
        count = 0
        for item in self.groups:
            count += 1
            print(f'{count}. Title:{item.title}, Direction:{item.direction}')

    def upd_group(self):
        print(" Choose a group to update:\n")
        self.view_groups()
        kod=int(input(" Enter group number:\n "))
        if 1<=kod<=len(self.groups):
            self.groups[kod-1].update_group()
        else:
            print("Invalid group number")
            return

    def delete_group(self):
        print(" Choose a group to delete:\n")
        self.view_groups()
        kod=int(input(" Enter group number:\n "))
        if 1<=kod<=len(self.groups):
            self.groups.pop(kod-1)
        else:
            print("Invalid group number")
            return
    def update_uni(self):
        self.title = input(" Enter new title:\n ")

class HEMIS:
    def __init__(self):
        self.title = 'HEMIS'
        self.uni = []

    def add_uni(self):
        title = input('title:')
        uni = Uni(title)
        self.uni.append(uni)

    def view_unis(self):
        count = 0
        for item in self.uni:
            count += 1
            print(f'{count}. title:{item.title}')

    def upd_uni(self):
        print(" Choose a uni to update:\n")
        self.view_unis()
        kod=int(input(" Enter uni number:\n "))
        if 1<=kod<=len(self.uni):
            self.uni[kod-1].update_uni()
        else:
            print("Invalid uni number")
            return

    def delete_uni(self):
        print(" Choose a uni to delete:\n")
        self.view_unis()
        kod=int(input(" Enter uni number:\n "))
        if 1<=kod<=len(self.uni):
            self.uni.pop(kod-1)
        else:
            print("Invalid uni number")
            return



def student_manager(group: Group):
    while True:
        kod=input(" 1. Add student\n 2. View students\n 3. Update student\n 4. Delete student\n 5. Exit\n ")
        if kod == "1":
            group.add_student()
        elif kod == "2":
            group.view_students()
        elif kod == "3":
            group.update_students()
        elif kod == "4":
            break
        else:
            print("Invalid input")

def uni_manager(uni: Uni):
    while True:
        kod = input(' 1. Add group \n 2. View groups \n 3. Update group\n 4. Delete group\n 5. Exit \n ')
        if kod == '1':
            uni.add_group()
        elif kod == '2':
            uni.view_groups()
        elif kod == '3':
            uni.upd_group()
        elif kod == '4':
            uni.delete_group()
        elif kod == '5':
            break
        else:
            print('Invalid input')
            return


def hemis_manager(hemis:HEMIS):
    while True:
        kod = input(' 1. Add university \n 2. View universities \n 3. Update university\n 4. Delete university\n 5.Exit \n ')
        if kod == '1':
            hemis.add_uni()
        elif kod == '2':
            hemis.view_unis()
        elif kod=='3':
            hemis.upd_uni()
        elif kod == '4':
            hemis.delete_uni()
        elif kod == '5':
            break
        else:
            print('Invalid input')
            return
def main():
    while True:
        kod=input(" 1. Student settings\n 2. Group settings\n 3. University settings\n 4. Exit\n ")
        if kod == '1':
            student_manager(Student)
        elif kod == '2':
            uni_manager(Uni)
        elif kod == '3':
            hemis_manager(HEMIS)
        elif kod == '4':
            break
        else:
            print('Invalid input')
            return


hemis=HEMIS()
main()
