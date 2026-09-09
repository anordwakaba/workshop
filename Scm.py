class Student :
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):
        return self.grade >= 60

class Club:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, student):
        if isinstance(student, Student):
            self.members.append(student)
            print(f"{student.name} has been added to the {self.name} club.")
        else:
            print("Only students can be added to the club.")

    def list_members(self):
        print(f"Members of {self.name} club:")
        for member in self.members:
            print(member.get_details())

student1 = Student("Alice", 16, 85)
student2 = Student("Bob", 15, 55)

math_club = Club("Math Club")
math_club.add_member(student1)
math_club.add_member(student2)
math_club.list_members()