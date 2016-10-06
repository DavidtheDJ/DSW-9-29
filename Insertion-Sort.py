#David Justice
#10-5-16
#Insertion Sort


#Defines new "insertionSort" function with parameter "List"
def insertionSort(List):

    #For loop runs until the end of "list" is reached
    for i in range(1,len(List)):

        #Variable currentValue holds current value of integer in list
        currentValue = List[i]
        #Variable holds postition of insert, taking position data from the For Loop
        position = i
        #Variable stores number of comparisions done
        comparisions = 0
            
        #While loop checks - if "position" is more than 0 and if
        #the integer left of insert is more than the "currentValue"(integer right of insert)
        while position > 0 and List[position-1] > currentValue:
            
            #Integer is moved back one space in list "List"
            List[position] = List[position - 1]
            #Insert position moves back one space
            position = position - 1

            #for each comparision done, "comparisions" increases by 1
            comparisions = comparisions + 1
        
        #List "position"(current integer) is updated to new value
        List[position] = currentValue

    #returns new "List" and comparisions done after For loop ends
    return comparisions, List


#Defines start fuction 
def start():

    #Creates a new unsorted integer list
    unsortedList = [7,3,1,4,2,6,5,6,9,1,3,1]
    
    #Variable "comparisions" stores returned value "comparisions"
    #Variable "sortedList" calls function "insertionSort" with parameter "unsortedList" list
    #Stores returned sorted list
    comparisions, sortedList = insertionSort(unsortedList)

    #converts variable "sortedList" integers to string and prints
    print(str(sortedList))
    #converts variable "comparisions" integers to string and prints 
    print(str(comparisions))


#calls function "start"
start()
