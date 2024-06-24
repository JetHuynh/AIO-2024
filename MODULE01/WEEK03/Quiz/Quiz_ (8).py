# Câu hỏi 8 Một Ward gồm có name (string) và danh sách của mọi người trong Ward. Một người person có thể là student, doctor, hoặc teacher và cần sử dụng một list để chứa danh sách của mọi người trong Ward. Viết add_person(person) method trong Ward class để add thêm một người mới với nghề nghiệp bất kỳ (student, teacher, doctor) vào danh sách người của ward. Tạo ra một ward object, và thêm vào 1 student, 2 teacher, và 2 doctor. Thực hiện describe() method để in ra tên ward (name) và toàn bộ thông tin của từng người trong ward. Chọn đáp án đúng nhất bên dưới cho phương thức đếm số lượng doctor.

from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        # Your Code Here
        super().__init__(name, yob)
        self.__grade = grade
        # End Code Here

    def describe(self):
        # Your Code Here
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")
        # End Code Here


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        # Your Code Here
        super().__init__(name, yob)
        self.__subject = subject
        # End Code Here

    def describe(self):
        # Your Code Here
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")
        # End Code Here


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        # Your Code Here
        super().__init__(name, yob)
        self.__specialist = specialist
        # End Code Here

    def describe(self):
        # Your Code Here
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")
        # End Code Here


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Ward Name : {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        # Your Code Here
        count = 0
        for person in self.__list_people:
            if isinstance(person, Doctor):
                count += 1
        return count
        # End Code Here


student1 = Student(name=" studentA ", yob=2010, grade="7")
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")

doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
assert ward1.count_doctor() == 1
ward1.add_person(doctor2)
print(ward1.count_doctor())
