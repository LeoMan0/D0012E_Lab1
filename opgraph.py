from stack import Stack
from sort import Sort  # Import your Sort class
import time
import matplotlib.pyplot as plt

def main():
    dataset_sizes = [1, 10, 100, 1000, 10000]
    operations = []  # Store the number of operations for each dataset size

    for size in dataset_sizes:
        print(f"\nTesting with dataset size: {size}")

        data = generateData(size)

        input_stack = Stack()
        for item in data:
            input_stack.push(item)

        sorter = Sort()

        sorted_stack = sorter.opsortStack(input_stack)

        op = sorter.getOpcount()
        operations.append(op)

        print(f"Number of operations for worst case: {op} operations")

    # Plot the results
    plot_operations(dataset_sizes, operations)


def generateData(n):
    # return list(range(1, n + 1))  # Uncomment for best case
    return list(range(n, 0, -1))  # Worst case: descending order


def plot_operations(sizes, measured_ops):
    plt.figure(figsize=(10, 6))

    # Plot measured operations
    plt.plot(sizes, measured_ops, 'o-', label='Measured Operations')

    plt.xscale('log')
    plt.yscale('log')
    # Add labels, legend, and title
    plt.xlabel('Dataset Size (n)')
    plt.ylabel('Number of Operations')
    plt.title('Operations on Sorting Algorithm for worst case')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()

