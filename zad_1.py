
class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


student_kania = Student("Szymon Kania", [75, 30, 89, 56])
print(student_kania.is_passed())

student_bolo = Student("Dawid Bolo", [0, 30, 15, 25])
print(student_bolo.is_passed())
