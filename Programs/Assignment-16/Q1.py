class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__major = major

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major


class Professor(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__department = department

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department


students = []
professors = []

def add_student(name, age, student_id, major):
    student = Student(name, age, student_id, major)
    students.append(student)

def add_professor(name, age, employee_id, department):
    professor = Professor(name, age, employee_id, department)
    professors.append(professor)

def display_all_students():
    for student in students:
        print(f"Name: {student.get_name()}, Age: {student.get_age()}, Student ID: {student.get_student_id()}, Major: {student.get_major()}")

def display_all_professors():
    for professor in professors:
        print(f"Name: {professor.get_name()}, Age: {professor.get_age()}, Employee ID: {professor.get_employee_id()}, Department: {professor.get_department()}")
