"""## Câu hỏi 11: Thực hiện xây dựng class Queue với các chức năng (method) sau đây: initialization method nhận một input "capacity", dùng để khởi tạo queue với capacity là số lượng element mà queue có thể chứa. Phương thức is_full(): kiểm tra queue đã full chưa. Phương thức enqueue(value) add thêm value vào trong queue. Kết quả đầu ra là gì?"""


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        # Your Code Here
        if self.is_full():
            raise IndexError("Queue is full")
        self.__queue.append(value)
        # End Code Here


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())
