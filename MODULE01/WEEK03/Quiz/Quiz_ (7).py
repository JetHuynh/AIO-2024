"""## Câu hỏi 7: Một người (person) có thể là student, doctor, hoặc teacher. Một doctor gồm có name (string), yob (string), và specialist (string). Các bạn thực hiện viết class Teacher theo mô tả trên (Các bạn sẽ viết thêm describe() method để print ra tất cả thông tin của object) và kết quả đầu ra là gì? Chọn đáp án đúng nhất bên dưới."""

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


doctor1 = Doctor(name=" doctorZ2023 ", yob=1981,
                 specialist=" Endocrinologists ")
assert doctor1._yob == 1981
doctor1.describe()
