
from typing import List


class Library:
    def __init__(self, city: str, street: str,
                 zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Library in {self.city}' \
               f' {self.zip_code} is located on {self.street}'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str,
                 birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f'{self.first_name} ' \
               f'{self.last_name} was hired on {self.hire_date}'


class Book:
    def __init__(self, title: str, library: Library, publication_date: str,
                 author_name: str, author_surname: str, number_of_pages: int):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f'{self.title} {self.author_name} ' \
               f'{self.publication_date} is located in ' \
               f'{self.library.city} - {self.library.street}'


class Student:
    def __init__(self, first_name: str, last_name: str, pesel: str):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel

    def __str__(self) -> str:
        return f'Student: {self.first_name} {self.last_name} | {self.pesel}'


class Order:
    def __init__(self, employee: Employee, student: str,
                 books: List[Book], order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Order was made on {self.order_date} ' \
               f'by {self.student} and is ' \
               f'assigned to {self.employee.first_name} ' \
               f'{self.employee.last_name}'


library_tichau = Library("Tychy", "Biblioteczna 8",
                         "43-100", "10:00 - 18:00", "123 456 789")
print(library_tichau.__str__())
library_gleiwitz = Library("Gliwice", "Akademicka 50",
                           "44-100", "08:00 - 15:30", "148 821 370")
print(library_gleiwitz.__str__())

student0 = Student("Bolo", "Janda", "11111111111")
print(student0.__str__())
student1 = Student("Michał", "Melaxes", "22222222222")
print(student1.__str__())

employee0 = Employee("Dawid", "Janda", "01.01.2020", "12.03.1997",
                     "Kobiur", "Rolna 12", "50-203", "262683257")
print(employee0.__str__())
employee1 = Employee("Martynka", "Cuteuwu", "23.04.2018", "01.10.1990",
                     "Jaworzno", "Jarzynowa 7/44", "24-123", "666666666")
print(employee1.__str__())
employee2 = Employee("Jan", "Nowak", "11.11.2022", "12.12.1989",
                     "Tychy", "Górna 15", "43-100", "123456789")
print(employee2.__str__())

book0 = Book("Granica", library_tichau, "Zofia", "Nałkowska", "1935", 333)
print(book0.__str__())
book1 = Book("W pustyni i w puszczy",
             library_gleiwitz, "Henryk", "Sienkiewicz", "1911", 268)
print(book1.__str__())
book2 = Book("Krzyżacy", library_tichau, "Henryk", "Sienkiewicz", "1900", 1410)
print(book2.__str__())
book3 = Book("Lemegeton", library_gleiwitz, "anonim", "", "XVII wiek", 666)
print(book3.__str__())
book4 = Book("Systemy ekspertowe", library_tichau,
             "Krzysztof", "michalik", "2014", 237)
print(book4.__str__())

order0 = Order(employee0, student1, [book4, book2], "18.10.2022")
print(order0.__str__())
order1 = Order(employee2, student1, [book0], "17.10.2022")
print(order1.__str__())
