from stack import Stack

class Sort:
    def __init__(self):
        pass

    def sortStack(self, inputStack):
        tempStack = Stack()
        #Whil is not empty
        while not inputStack.isEmpty():
            rightHand = inputStack.pop()

            if tempStack.isEmpty():
                tempStack.push(rightHand)
            
            else:
                leftHand = tempStack.pop()
                #tempStack.push(leftHand)

                while not tempStack.isEmpty() and leftHand >= rightHand:
                    inputStack.push(leftHand)
                    leftHand = tempStack.pop()

                tempStack.push(leftHand)
                tempStack.push(rightHand)

        return tempStack
