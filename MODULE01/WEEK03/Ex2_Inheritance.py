# Python OOP - Inheritance
'''
Person:
  - name
  - yob
Student:
  - Person
  - grade
Teacher:
  - Person
  - subject
Doctort:
  - Person
  - specialization
Ward:
  - name
  - List[Person]
'''

from abc import ABC, abstractmethod

# Class Person (class abstract)


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_name(self):
        return self._name

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

# class Student


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")

# class Doctor


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")

# class Teacher


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")

# class Ward


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__list_person = []

    def add_person(self, person: Person):
        self.__list_person.append(person)

    def describe(self):
        print(f"Ward - Name: {self.__name}")
        for person in self.__list_person:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__list_person:
            if isinstance(person, Doctor):
                count += 1
        return count

    def count_teacher(self):
        count = 0
        for person in self.__list_person:
            if isinstance(person, Teacher):
                count += 1
        return count

    def count_student(self):
        count = 0
        for person in self.__list_person:
            if isinstance(person, Student):
                count += 1
        return count

    def sort_age(self):
        self.__list_person.sort(key=lambda x: x.get_yob())

    def compute_average_teacher_age(self):
        total_age = 0
        count = 0
        for person in self.__list_person:
            if isinstance(person, Teacher):
                total_age += person.get_yob()
                count += 1

        if count > 0:
            return int(total_age / count)
        else:
            return 0


# Examples
# 2(a)
print('\nEx 2.a:')
student1 = Student("studentA", 2010, "7")
student1.describe()

teacher1 = Teacher("teacherA", 1969, "Math")
teacher1.describe()

doctor1 = Doctor("doctorA", 1945, "Endocrinologists")
doctor1.describe()

# 2(b)
print('\nEx 2.b:')
teacher2 = Teacher("teacherB", 1995, "History")
doctor2 = Doctor("doctorB", 1975, "Cardiologists")
ward1 = Ward("Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print('\nEx 2.c:')
print(f'Number of doctors : {ward1.count_doctor()}')

# 2(d)
print('\nEx 2.d:')
print("After sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# 2(e)
print('\nEx 2.e:')
print(
    f'Average year of birth (teachers): { ward1.compute_average_teacher_age()}')
