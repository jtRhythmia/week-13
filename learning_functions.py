numbers = 7,175,25,37

def findMaxInList(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return(max_value)

print(findMaxInList(numbers))
    



