"""## Câu hỏi 6: Một người (person) có thể là student, doctor, hoặc teacher. Một teacher gồm có name (string), yob (int), và subject (string). Các bạn thực hiện viết class Teacher theo mô tả trên (Các bạn sẽ viết thêm describe() method để print ra tất cả thông tin của object) và kết quả đầu ra là gì? Chọn đáp án đúng nhất bên dưới."""

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


teacher1 = Teacher(name=" teacherZ2023 ", yob=1991, subject=" History ")
assert teacher1._yob == 1991
teacher1.describe()
