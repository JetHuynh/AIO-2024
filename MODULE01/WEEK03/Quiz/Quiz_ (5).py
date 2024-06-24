"""## Câu hỏi 5: Một người (person) có thể là student, doctor, hoặc teacher. Một student gồm có name (string), yob (int) (năm sinh), và grade (string). Các bạn thực hiện viết class Student theo mô tả trên (Các bạn sẽ viết thêm describe() method để print ra tất cả thông tin của object) và kết quả đầu ra là gì? Chọn đáp án đúng nhất bên dưới"""

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


student1 = Student(name=" studentZ2023 ", yob=2011, grade="6")
assert student1._yob == 2011
student1.describe()
