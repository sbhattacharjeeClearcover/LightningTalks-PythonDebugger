import random


def addition(a, b):
    result = a + b
    return result


def multiplication(a, b):
    result = a * b
    return result


number_list = [6, 8, 1]
def add_list(array: list):
    result = 0
    for i in range(len(number_list)):
        random_int = random.randint(0, 10)
        result += array[i]
    return random_int, result


if __name__ == '__main__':

    # Simple Step Over, Resume Program, Run to Cursor, Show Execution Point, Stop
    print("Printing Statement 1...")
    print("Printing Statement 2...")
    print("Printing Statement 3...")
    print("Printing Statement 4...")
    print("Printing Statement 5...")

    # Simple Step Over, Step Into
    # (1 x 2) + 3 = 5
    print('Output using helpers divide function for (1 x 2) + 3 = 5: ', addition(multiplication(1, 2), 3))

    # User-defined module: Step Into My Code
    from debug_helpers.math_ops import add, multiply, divide
    # (3 x 2) + 4 = 10
    print(add(multiply(3, 2), 4))

    # Built-in module: Step Into vs Step Into My Code, Step Over = Step Into My Code
    print(add_list(number_list))

    # User-defined module: Step Over vs Step Into My Code, Step into = Step Into My Code
    # ((6 + 4) * 5)/2 = 25

    print('Output using helpers divide function for ((6 + 4) * 5)/2: ', divide(multiply(add(6, 4), 5), 2))
    print('Output without helpers divide function for ((6 + 4) * 5)/2: ', multiply(add(6, 4), 5)/2)

