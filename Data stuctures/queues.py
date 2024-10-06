from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f'Enqueued {item} to queue')

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.popleft()
            print(f'Dequeued {removed_item} from queue')
            return removed_item
        else:
            print('Queue is empty')
            return None

    def front(self):
        if not self.is_empty():
            print(f'Front element is {self.queue[0]}')
            return self.queue[0]
        else:
            print('Queue is empty')
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def task_scheduler(tasks: list):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)

    while not queue.is_empty():
        current_task = queue.dequeue()
        print(f'Processing task: {current_task}')


def supermarket_checkout(customers: list):
    queue = Queue()
    for customer in customers:
        queue.enqueue(customer)

    while not queue.is_empty():
        current_customer = queue.dequeue()
        print(f'Customer {current_customer} is at the casher.')


# customers = ['Monica', 'Lisa', 'Dafne']
# supermarket_checkout(customers)

# customers = ["Customer 1", "Customer 2", "Customer 3"]
# customers = ["Customer A", "Customer B", "Customer C", "Customer D",
#              "Customer E"]
# customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
# customers = ["Customer 1", "Customer 2", "Customer 1", "Customer 3",
#              "Customer 2"]
# customers = []
# customers = ["Solo Customer"]


# supermarket_checkout(customers)


