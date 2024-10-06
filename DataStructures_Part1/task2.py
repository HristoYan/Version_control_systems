class Stack:
    def __init__(self, length):
        self.length = length
        self.stack = []

    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
            print(f'Pushed to {item} to stack')
        else:
            print('The stack is full!')

    def pop(self):
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f'Pooped {removed_item} from stack')
            return removed_item
        else:
            print('Stack is empty')
            return None

    def peek(self):
        if not self.is_empty():
            print(f'Pooped {self.stack[-1]} from stack')
            return self.stack[-1]
        else:
            print('Stack is empty')
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.length

    def size(self):
        return len(self.stack)

    def clear_stack(self):
        self.stack = []
        return 'The stack is empty!'


def main():
    stack_len = int(input('Stack\'s length: '))
    my_stack = Stack(stack_len)
    while True:
        print('What do you want to do now?')
        choice = input('add, extract, length, empty, full, clear, peek or exit: ')
        if choice == 'add':
            value = input('Content: ')
            my_stack.push(value)
        elif choice == 'extract':
            print(my_stack.pop())
        elif choice == 'length':
            print(my_stack.size())
        elif choice == 'empty':
            print(my_stack.is_empty())
        elif choice == 'full':
            print(my_stack.is_full())
        elif choice == 'clear':
            print(my_stack.clear_stack())
        elif choice == 'peek':
            print(my_stack.peek())
        elif choice == 'exit':
            break
        else:
            print('Improper input!')


main()