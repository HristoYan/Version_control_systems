from collections import deque


class ServerQueue:
    def __init__(self):
        self.server_queue = deque()
        self.high_sever_queue = deque()
        self.low_server_queue = deque()
        self.stat = deque()

    def request_queue(self, request, priority):
        if priority == 'high':
            self.high_sever_queue.append(request)
            self.stat.append({request: priority})
        else:
            self.low_server_queue.append(request)
            self.stat.append({request: priority})

        self.server_queue = self.high_sever_queue + self.low_server_queue
        return self.server_queue

    def execution(self):
        if not self.is_empty():
            value = self.server_queue.popleft()
            self.stat.append({'out': value})
            return f'Request {value} executed!'

        else:
            print('Queue is empty')
            return None

    def see_stat(self):
        print('Statistics: ')
        for info in self.stat:

            print(info)

    def is_empty(self):
        return len(self.server_queue) == 0


def server_client(requests: list):
    queue = ServerQueue()
    if requests:
        for request in requests:
            queue.request_queue(request['request'], request['priority'])

    while not queue.is_empty():
        print(queue.execution())

    queue.see_stat()


requests = [{'request': 'req1', 'priority': 'low'},
            {'request': 'req2', 'priority': 'high'},
            {'request': 'req3', 'priority': 'low'},
            {'request': 'req4', 'priority': 'high'},
            {'request': 'req5', 'priority': 'low'}]

server_client(requests)
