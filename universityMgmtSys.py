'''
    CPP 6102: COMPUTATIONAL THINKING & PROGRAMMING FOR DATA SCIENCE
    GROUP 6
    ASSIGNMENT ONE
'''


class Member:
    def __init__(self, name, id, contact_information):
        self.name = name
        self.id = id
        self.contact_information = contact_information
    
    def display_info(self):
        print(f"\n\nName: {self.name}, ID: {self.id}, Contact: {self.contact_information}")

class Student(Member):
    def __init__(self, name, id, contact_information, major, year):
        super().__init__(name, id, contact_information)
        self.major = major
        self.year = year
    
    def display_info(self):
        super().display_info()
        print(f"Major: {self.major}, Year: {self.year}")


class TeachingStaff(Member):
    def __init__(self, name, id, contact_information, department, designation):
        super().__init__(name, id, contact_information)
        self.department = department
        self.designation = designation
    
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}, Designation: {self.designation}")

class NonTeachingStaff(Member):
    def __init__(self, name, id, contact_information, role, department):
        super().__init__(name, id, contact_information)
        self.role = role
        self.department = department
    
    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}, Department: {self.department}")


student = Student("Alice", "S001", "alice@example.com", "Computer Science", 2)
student.display_info()

print("\n")

teaching_staff = TeachingStaff("Dr. Smith", "T001", "smith@example.com", "Physics", "Lecturer")
teaching_staff.display_info()

second_teaching_staff = TeachingStaff("Dr. Kevin Mugoye", "T002", "kevin@example.com", "Computational Thinking", "Lecturer")
second_teaching_staff.display_info()

print("\n")

non_teaching_staff = NonTeachingStaff("John Doe", "NT001", "john@example.com", "Administrator", "HR")
non_teaching_staff.display_info()

print("\n")


# print(isinstance(student, Student))
# print(issubclass(Student, Member))