'''
Thực hiện xây dựng class Queue với các chức năng (method) sau đây
• initialization method nhận một input "capacity": dùng để khởi tạo queue với capacity là
số lượng element mà queue có thể chứa
• .is_empty(): kiểm tra queue có đang rỗng
• .is_full(): kiểm tra queue đã full chưa
• .dequeue(): loại bỏ first element và trả về giá trị đó
• .enqueue(value) add thêm value vào trong queue
• .front() lấy giá trị first element hiện tại của queue, nhưng không loại bỏ giá trị đó
• Không cần thiết phải thực hiện với các pointers như trong hình minh họa
'''


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
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__queue[0]

  # run example


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())


print('\n')
queue2 = MyQueue(capacity=2)
queue2.enqueue(1)
queue2.enqueue(2)
print(queue2.front())
print(queue2.is_full())
print(queue2.dequeue())
print(queue2.dequeue())
print(queue2.is_empty())


print('\n')
queue1 = MyQueue(capacity=2)
queue1.enqueue(1)
queue1.enqueue(2)
# queue1.enqueue(2) #error
