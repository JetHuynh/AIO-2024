"""## Câu hỏi 12: Thực hiện xây dựng class Queue với các chức năng (method) sau đây: initialization method nhận một input "capacity" dùng để khởi tạo queue với capacity là số lượng element mà queue có thể chứa. Phương thức is_full(): kiểm tra queue đã full chưa. Phương thức enqueue(value) add thêm value vào trong queue. Phương thức front() lấy giá trị first element hiện tại của queue, nhưng không loại bỏ giá trị đó. Kết quả đầu ra là gì?"""


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise IndexError("Queue is full")
        self.__queue.append(value)

    def front(self):
        # Your Code Here
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__queue[0]
        # End Code Here


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.front())
