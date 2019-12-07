number = list(map(int, input().split(" ")))

def printOrder(number):
    ascending = True
    descending = True
    for i in range(0, len(number) - 1):
        if number[i+1] < number[i]:
            ascending = False #ascending
        elif number[i+1] > number[i]:
            descending = False #descending

    if ascending:
        print("Ascending")
    elif descending:
        print("Descending")
    else:
        print("Mixed")

printOrder(number)