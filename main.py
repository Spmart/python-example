# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0
    for number in numbers:
        print(number)
        sum += number
    print(sum)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(fact(5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
