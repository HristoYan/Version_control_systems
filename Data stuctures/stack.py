class Stack:
    def __init__(self):
        self.stack = []

    def puch(self, item):
        self.stack.append(item)
        print(f'Pushed to {item} to stack')

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

    def size(self):
        return len(self.stack)


def reverse_str(input_str):
    stack = Stack()
    for char in input_str:
        stack.puch(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


# my_str = reverse_str('Hello, world')
# print(my_str)


def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in '([{':
            stack.puch(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            top = stack.pop()

            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False

    return stack.is_empty()


# print(is_balanced('([{}])'))

# print(is_balanced('([)]'))
# “[({})]”
# “({[()]})”
# “({[}])”
# “(((())))”
# “([)]”
# “{[()()]}”
# “[(])”
# “{{{{[[[]]]]}}}”
# “{{[[(())]]}}”
# “([{}])({})”
# “{{[[(())]]]}”