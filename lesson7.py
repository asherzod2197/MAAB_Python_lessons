# ======================================================
# 1. GENERALIZED VECTOR CLASS
# ======================================================

import math

class Vector:

    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have same dimension")

    # Addition
    def __add__(self, other):
        self.check_dimension(other)
        return Vector(*[a+b for a,b in zip(self.components, other.components)])

    # Subtraction
    def __sub__(self, other):
        self.check_dimension(other)
        return Vector(*[a-b for a,b in zip(self.components, other.components)])

    # Dot product OR scalar multiplication
    def __mul__(self, other):

        if isinstance(other, Vector):
            self.check_dimension(other)
            return sum(a*b for a,b in zip(self.components, other.components))

        else:
            return Vector(*[a*other for a in self.components])


    def __rmul__(self, scalar):
        return self * scalar


    def magnitude(self):
        return math.sqrt(sum(a*a for a in self.components))


    def normalize(self):

        mag = self.magnitude()

        if mag == 0:
            raise ValueError("Zero vector cannot be normalized")

        return Vector(*[round(a/mag,3) for a in self.components])


# Example
print("=== VECTOR EXAMPLE ===")

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

print(v1)
print(v1+v2)
print(v2-v1)
print(v1*v2)
print(3*v1)
print(v1.magnitude())
print(v1.normalize())



# ======================================================
# 2. EMPLOYEE RECORDS MANAGER (OOP)
# ======================================================


class Employee:

    def __init__(self, employee_id, name, position, salary):

        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary


    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"



class EmployeeManager:

    FILE = "employees.txt"


    def add_employee(self):

        emp_id = input("Employee ID: ")

        if self.exists(emp_id):
            print("Employee ID already exists")
            return

        name = input("Name: ")
        position = input("Position: ")
        salary = input("Salary: ")


        emp = Employee(emp_id,name,position,salary)

        with open(self.FILE,"a") as f:
            f.write(str(emp)+"\n")

        print("Employee added successfully")


    def exists(self, emp_id):

        try:
            with open(self.FILE) as f:
                for line in f:
                    if line.startswith(emp_id+","):
                        return True
        except:
            return False

        return False



    def view_all(self):

        try:
            with open(self.FILE) as f:

                print("\nEmployee Records")

                for line in f:
                    print(line.strip())

        except:
            print("No records")


    def search(self):

        emp_id = input("Employee ID: ")

        with open(self.FILE) as f:

            for line in f:

                if line.startswith(emp_id+","):
                    print("Found:",line)
                    return

        print("Not found")



    def update(self):

        emp_id = input("Employee ID: ")

        new_lines=[]

        found=False

        with open(self.FILE) as f:

            for line in f:

                if line.startswith(emp_id+","):

                    name=input("New name:")
                    pos=input("New position:")
                    sal=input("New salary:")

                    new_lines.append(f"{emp_id}, {name}, {pos}, {sal}\n")

                    found=True

                else:
                    new_lines.append(line)



        with open(self.FILE,"w") as f:

            f.writelines(new_lines)

        if found:
            print("Updated")
        else:
            print("Not found")



    def delete(self):

        emp_id=input("Employee ID:")

        new_lines=[]

        found=False

        with open(self.FILE) as f:

            for line in f:

                if line.startswith(emp_id+","):
                    found=True
                    continue

                new_lines.append(line)


        with open(self.FILE,"w") as f:

            f.writelines(new_lines)

        if found:
            print("Deleted")
        else:
            print("Not found")



    def menu(self):

        while True:

            print("\nEMPLOYEE MANAGER")

            print("1 Add")
            print("2 View")
            print("3 Search")
            print("4 Update")
            print("5 Delete")
            print("6 Exit")

            ch=input("Choice:")

            if ch=="1":
                self.add_employee()

            elif ch=="2":
                self.view_all()

            elif ch=="3":
                self.search()

            elif ch=="4":
                self.update()

            elif ch=="5":
                self.delete()

            elif ch=="6":
                break



# ======================================================
# 3. TODO APPLICATION
# ======================================================

import json
import csv



class Task:

    def __init__(self,id,title,desc,date,status):

        self.id=id
        self.title=title
        self.desc=desc
        self.date=date
        self.status=status


    def to_dict(self):

        return vars(self)


    def __str__(self):

        return f"{self.id}, {self.title}, {self.desc}, {self.date}, {self.status}"



# File strategy base class
class Storage:

    def save(self,tasks):
        pass

    def load(self):
        pass



class JSONStorage(Storage):

    FILE="tasks.json"

    def save(self,tasks):

        with open(self.FILE,"w") as f:

            json.dump([t.to_dict() for t in tasks],f)


    def load(self):

        try:
            with open(self.FILE) as f:

                data=json.load(f)

                return [Task(**d) for d in data]

        except:
            return []



class CSVStorage(Storage):

    FILE="tasks.csv"

    def save(self,tasks):

        with open(self.FILE,"w",newline="") as f:

            writer=csv.writer(f)

            for t in tasks:
                writer.writerow([t.id,t.title,t.desc,t.date,t.status])



    def load(self):

        tasks=[]

        try:
            with open(self.FILE) as f:

                reader=csv.reader(f)

                for r in reader:
                    tasks.append(Task(*r))

        except:
            pass

        return tasks



class TodoApp:

    def __init__(self,storage):

        self.storage=storage

        self.tasks=self.storage.load()



    def add(self):

        id=input("Task ID:")
        title=input("Title:")
        desc=input("Desc:")
        date=input("Date:")
        status=input("Status:")

        self.tasks.append(Task(id,title,desc,date,status))


    def view(self):

        for t in self.tasks:
            print(t)


    def update(self):

        id=input("Task ID:")

        for t in self.tasks:

            if t.id==id:

                t.title=input("New title:")
                t.desc=input("New desc:")
                t.date=input("New date:")
                t.status=input("New status:")

                return


    def delete(self):

        id=input("Task ID:")

        self.tasks=[t for t in self.tasks if t.id!=id]


    def filter(self):

        status=input("Status:")

        for t in self.tasks:

            if t.status==status:
                print(t)


    def save(self):
        self.storage.save(self.tasks)


    def load(self):
        self.tasks=self.storage.load()


    def menu(self):

        while True:

            print("\nTODO APP")

            print("1 Add")
            print("2 View")
            print("3 Update")
            print("4 Delete")
            print("5 Filter")
            print("6 Save")
            print("7 Load")
            print("8 Exit")

            c=input("Choice:")

            if c=="1":
                self.add()

            elif c=="2":
                self.view()

            elif c=="3":
                self.update()

            elif c=="4":
                self.delete()

            elif c=="5":
                self.filter()

            elif c=="6":
                self.save()

            elif c=="7":
                self.load()

            elif c=="8":
                break



# ======================================================
# MAIN MENU
# ======================================================

print("\nSelect Program")

print("1 Vector Example")
print("2 Employee Manager")
print("3 Todo App JSON")
print("4 Todo App CSV")

choice=input("Choice:")


if choice=="2":

    EmployeeManager().menu()

elif choice=="3":

    TodoApp(JSONStorage()).menu()

elif choice=="4":

    TodoApp(CSVStorage()).menu()

else:

    print("Finished")