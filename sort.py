from stack import Stack

class Sort:
    def __init__(self):
        self.opcount = 0

    #Outer 1 + 2 + 2
    # Inner 4 
    # 4*5=20*n

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

    def opsortStack(self, inputStack):
        tempStack = Stack()

        while not inputStack.isEmpty():
            #One operation for isEmpty
            self.opcount += 1
            rightHand = inputStack.pop()
            #Two ops for for pop and writting times two
            leftHand = tempStack.pop()
            self.opcount += 2


            while leftHand is not None and leftHand < rightHand:
                self.opcount += 2
                inputStack.push(leftHand)
                self.opcount += 1
                leftHand = tempStack.pop()
                self.opcount += 1
            self.opcount += 2
            if leftHand is not None:
                tempStack.push(leftHand)
                self.opcount += 2
            tempStack.push(rightHand)
            self.opcount +=1
        return tempStack

    def getOpcount(self):
        return self.opcount
