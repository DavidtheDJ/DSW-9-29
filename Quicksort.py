#David Justice
#10-5-16
#Quicksort

#Code was supplied
#Only needed to add counter




def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    
    # Start outside the area to be partitioned
    right = end
    done = False
    
    while not done:
        
#########################################################################
        #Everytime while loop loops, adds 1 one to global variable "myCounter"
        global myCounter
        myCounter = myCounter + 1
#########################################################################
        
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp

    return right





def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList


def main():
    myList = [7,2,5,1,29,6,4,19,11]
    
#########################################################################
    #defines a new global variable called my counter to count number o
    #comparisions done
    global myCounter
    myCounter = 0
#########################################################################
    
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)
    
#########################################################################
    #prints "myCounter"
    print(myCounter)
#########################################################################

main()



