# Program to implement, test and benchmark sorting algorithm
# deviced by Niklas Winde in 2018, called NSort

import random

random.seed()


for j in range(10):
    toBeSorted = []
    sortedList = []

    operations = 1

    for i in range(1000):
        toBeSorted.append(random.randint(0, 100))

    while len(toBeSorted) > 0:
        item = toBeSorted.pop()

        # No items yet in sorted list
        if (len(sortedList) == 0):
            sortedList.append(item)
            #print ("added first")
            continue

        # Items fits outside sorted list
        if (item <= sortedList[0]):
            sortedList.insert(0, item)
            #print ("inserting")
            operations += 1
            continue
        elif (item >= sortedList[-1]):
            sortedList.append(item)
            #print ("appending")
            operations += 1
            continue

        # Must iterate to find place in array
        #print ("iterating")
        found = False
        index = 0
        while (found == False):
            operations += 1
            if ((item > sortedList[index]) and (item <= sortedList[index + 1])):
                sortedList.insert(index + 1, item)
                found = True
                #print ("iterated")
            else:
                index += 1

        
    print ("operations: " + str(operations))