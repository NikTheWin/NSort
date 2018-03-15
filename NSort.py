# Program to implement, test and benchmark sorting algorithm
# deviced by Niklas Winde in 2018, called NSort

import random

random.seed()

# Iterates a number of times for test purposes
for j in range(10):
    toBeSorted = []
    sortedList = []

    operations = 2 # First two operations happen outside loop

    # Generate random test list
    for i in range(100000):
        toBeSorted.append(random.randint(0, 100))

    # No items yet in sorted list
    item = toBeSorted.pop()
    sortedList.append(item)
    
    # Second item to sorted list
    item = toBeSorted.pop()
    # Item fits outside sorted list (it always does for second item)
    if (item <= sortedList[0]):
        sortedList.insert(0, item)
    elif (item >= sortedList[-1]):
        sortedList.append(item)
    
    # Actually sort. TODO: Refactor
    # First 20 position is naïve regular iteration if items are inside sorted list
    for i in range(20):
        item = toBeSorted.pop()

        # Items fits outside sorted list
        if (item <= sortedList[0]):
            sortedList.insert(0, item)
            operations += 1
            continue
        elif (item >= sortedList[-1]):
            sortedList.append(item)
            operations += 1
            continue

        # Must iterate to find place in array
        found = False
        index = 0
        while (found == False):
            operations += 1
            if ((item > sortedList[index]) and (item <= sortedList[index + 1])):
                sortedList.insert(index + 1, item)
                found = True
            else:
                index += 1

    # Rest of items use binary search in iterations
    while len(toBeSorted) > 0:
        item = toBeSorted.pop()

        # Items fits outside sorted list
        if (item <= sortedList[0]):
            sortedList.insert(0, item)
            operations += 1
            continue
        elif (item >= sortedList[-1]):
            sortedList.append(item)
            operations += 1
            continue

        # Must iterate to find place in array
        found = False
        index = 0
        newIndex = (len(sortedList) - 1) // 2
        forward = True
        while (found == False):
            operations += 1

            if ((item > sortedList[index])):
                if (item <= sortedList[index + 1]):
                    sortedList.insert(index + 1, item)
                    found = True

                if (forward == False):
                    newIndex //= 2

                if newIndex == 0:
                    newIndex = 1

                index += newIndex

                Forward = True
            else:
                if (forward == True):
                    newIndex //= 2

                if newIndex == 0:
                    newIndex = 1
                
                index -= newIndex
                forward = False

            if index <= 0:
                index = 1
        
    print ("operations: " + str(operations))


for j in range(10):
    toBeSorted = []

    # Generate random test list
    for i in range(100000):
        toBeSorted.append(random.randint(0, 100))

    toBeSorted.sort()

    print("Gjort: " + str(j))    