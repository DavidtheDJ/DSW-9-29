#David Justice
#9-29-16
#Bubble Sort

#Defines function called bubbleSort
def bubbleSort(myList):
    
    #Creates counter variable to count number of comparisons 
    counter = 0
    #Creates boolean moreSwaps to contorl while loop runs 
    moreSwaps = True
    
    #while loop checks to see if variable moreSwaps is True
    while moreSwaps:
        
        #Sets moreSwaps to False
        moreSwaps = False

        #for loop runs until length of myList is reached
        for element in range(len(myList) - 1):
            
            #for every run of for loop, adds one to counter variable
            counter = counter + 1

            #if statment checks if each 2 items needs to be swapped
            if myList[element] > myList[element + 1]:
                
                #sets moreSwaps to True to continue running
                moreSwaps = True

                #Variable temp saves item to be over written 
                temp = myList[element]

                #swap is preformed by deleting number to be over written
                #then adding the temp after in the list
                myList[element] = myList[element + 1]
                myList[element + 1] = temp

    #returns the results of the swap in the list and the counts done to complete 
    return myList, counter


#Defines function called testBubbleSort
def testBubbleSort():

    #creates myList list
    myList = [12,5,7,18,11,6,12,4,17,1]

    #creates two variables, sortedList and counter, that call function bubbleSort and
    #store the returned list and count values.
    sortedList, counter = bubbleSort(myList)

    #prints sorted list 
    print(sortedList)
    
    #prints the returned number of comparisons done
    print("Counts = " + str(counter))


#Calls function testBubbleSort
testBubbleSort()
