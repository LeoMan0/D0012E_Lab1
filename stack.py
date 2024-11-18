class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.pointer = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError("Pop on empty Stack")
        pop = self.top
        self.top = pop.pointer
        return pop.data

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def _print_stack(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.pointer
        print('None')


class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None


def main():
    stack = Stack()

    print(stack.isEmpty()) 
    stack.push(1)
    print(stack.isEmpty())    
    stack.push(2)
    stack.push(3)

    stack._print_stack()
    i = stack.pop()
    stack._print_stack()
    stack.pop()
    stack.pop()
    print(stack.isEmpty()) 
    print (i)

if __name__ == '__main__':
    main()


