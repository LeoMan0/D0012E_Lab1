from stack import Stack
from sort import Sort  # Import your Sort class
import time
import random

def main():
    dataset_sizes = [100, 1000, 10000, 100000 ,10000000]
    input_stack = Stack()
    
    for size in dataset_sizes:
        print(f"\nTesting with dataset size: {size}")

        data = generateData(size)
        #data = generateRandom(size)

        input_stack = Stack()
        for item in data:
            input_stack.push(item)

        sorter = Sort()

        start_time = time.time()
        sorted=sorter.opsortStack(input_stack)
        end_time = time.time()

        execution_time = end_time - start_time
        op = sorter.getOpcount()

        print(f"Time taken to sort {size} elements: {execution_time:.4f} seconds, {op} operations")


def generateData(n):
    #return list(range(n, 0, -1))
    return list(range(0, n, 1))
def generateRandom(n):
    rand_list=[]
    for i in range(n):
        rand_list.append(random.randint(0,n))
    return rand_list

if __name__ == "__main__":
    main()

