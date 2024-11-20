from stack import Stack

class Sort:
    def __init__(self):
        pass


    def sortStack(self, inputStack):
        tempStack = Stack()

        while not inputStack.isEmpty():
            rightHand = inputStack.pop()
            leftHand = tempStack.pop()

            while leftHand is not None and leftHand < rightHand:
                inputStack.push(leftHand)
                leftHand = tempStack.pop()
            
            if leftHand is not None:
                tempStack.push(leftHand)
            tempStack.push(rightHand)

        return tempStack
