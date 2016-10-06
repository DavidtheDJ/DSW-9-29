#David Justice
#10-5-16
#Stacks


#Creates class "Stack"
class Stack:

    #defines function "__init__" with parameter self
    def __init__(self):
        #Creates stack list
        self.items = []

    #defines function "push" with parameters self and item
    def push(self,item):
        #Takes stack list and new item, adds the new item to the list
        self.items.append(item)

    #defines function "pop" with parameter self 
    def pop(self):
        #takes stack list and removes last item, returns new stack list
        return self.items.pop()

    #defines function "peek" with parameter self   
    def peek(self):
        #takes stack list and returns last item in stack list
        return self.items[len(self.items)-1]

    #defines function "size" with parameter self  
    def size(self):
        #takes stack list and returns length of stack list
        return len(self.items)
    
    #defines function "isEmpty" with parameter self   
    def isEmpty(self):
        #if statement tests if stack list is equal to 0 items 
        if self.items == []:
            #returns true is there are 0 items
            return True
        #else 
        else:
            #returns false if stack list length is more than 0
            return False


        
#defines function start
def start():
    #creates stack
    myStack = Stack()
    #adds "bob" to stack list
    myStack.push("Bob")
    #adds "Charles" to stack list
    myStack.push("Charles")
    #adds "John" to stack list
    myStack.push("John")
    #removes last item in stack list and stores return
    myString = myStack.pop()
    #checks for last item in stack list and stores return
    myPeekString = myStack.peek()

    #prints last item by taking variable myPeekString
    print("Last Item: " + myPeekString)
    #prints last item removed by taking variable myString
    print("Item removed: " + myString)
    #converts returned int to string and prints the length of stack list
    print("Items in List: " + str(myStack.size()))
    #prints whether the stack list is empty or not
    print("The stack is empty: " + str(myStack.isEmpty()))

#calls function start to begin
start()
