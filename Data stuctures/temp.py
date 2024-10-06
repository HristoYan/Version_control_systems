from stack import Stack
from queues import Queue


class TextEditor:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()

    def type_character(self, char):
        self.stack.puch(char)
        self.queue.enqueue(f'Typed {char}')

    def undo(self):
        if not self.stack.is_empty():
            char = self.stack.pop()
            self.queue.enqueue(f'Undo character {char}')
        else:
            print('Noting to undo')

    def proces_actions(self):
        while not self.queue.is_empty():
            action = self.queue.dequeue()
            print(action)


editor = TextEditor()
editor.type_character('a')
editor.type_character('b')
editor.type_character('c')
editor.undo()
editor.proces_actions()


