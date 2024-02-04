def fibonacci():
    value = int(input("Enter a number to find the fibonacci series"))
    n1, n2 = 0, 1
    for i in range(value):
        print(n1)
        fibonacciNumbers = n1 + n2
        n1 = n2
        n2 = fibonacciNumbers
        i += 1


# fibonacci()

def largestInList(arr, n):
    maximumNumber = max(arr)
    return maximumNumber


# arr = []
# totalCount = int(input("Enter total number"))
# for i in range(totalCount):
#     number = int(input("Enter number"))
#     arr.append(number)
# n = len(arr)
# print(largestInList(arr, n))


def reverseNumber():
    reverse = 0
    n = int(input("Number to Reverse"))

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    print(f"Reversed Number :{reverse}")


# reverseNumber()


def specificFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b


print(specificFibonacci(6))


def characterSearch(text):
    result = 0
    for i in text.lower():
        if i == "r":
            result += 1
    return result


print(characterSearch("river"))
