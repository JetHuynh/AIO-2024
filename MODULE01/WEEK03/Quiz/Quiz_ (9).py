"""## Câu hỏi 9 Thực hiện xây dựng class Stack với các chức năng (method) sau đây: initialization method nhận một input "capacity": dùng để khởi tạo stack với capacity là số lượng element mà stack có thể chứa. .is_full(): kiểm tra stack đã full chưa. .push(value) add thêm value vào trong stack. Kết quả đầu ra là gì?"""


class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        # Your Code Here
        if self.is_full():
            raise IndexError("Stack is full")
        self.__stack.append(value)
        # End Code Here


stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.is_full())
