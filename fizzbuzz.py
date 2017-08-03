import sys, argparse

#setup fallback values
count = 1
countLimit = 100
method = "ifelse"

#parse input arguments -m, method, -l, limit
parser = argparse.ArgumentParser()
parser.add_argument('-m','--method', help='Which FizzBuzz generation method to use')
parser.add_argument('-l','--limit',help='How many numbers to run FizzBuzz for', type=int)
args = parser.parse_args()

if args.method: method = args.method
if args.limit: countLimit = args.limit

#function to generate FizzBuzz using nested if and else statements with prints
def ifElseMethod(count):
    
    #loop through all the numbers to be checked up to, and including the limit
    while count <= countLimit:
    
        if count % 3 == 0:
            if count % 5 == 0:
                #if the countber is a multiple of both 3 and 5
                print("FizzBuzz")
            #if the countber is only a multiple of 3
            else: print("Fizz")
        #if the countber wasn't a multiple of 3 but is a multiple of 5
        elif count % 5 == 0:
            print ("Buzz")
        #if the countber is neither a multiple of 3 or 5
        else: print(count)
        
        count += 1

#function to generate FizzBuzz using just if statements and concatonating results for each number before printing
def stringConCatMethod(count):
    
    #loop through all the numbers to be checked up to, and including the limit
    while count <= countLimit:
    
        string = ""
        
        if count % 3 == 0:
            string += "Fizz"
        if count % 5 == 0:
            string += "Buzz"
        if count % 3 != 0 and count % 5 != 0: string += str(count)
        
        print(string)
        
        count += 1
    
def recursiveMethod():
    
    string = recursivePrint(0)
    
    #remove the leading "\n" to be character-accurate
    print(string.lstrip())
    
def recursivePrint(num):
    
    returnedString = ""
    
    num += 1
    
    #if this is not the last number to be checked
    if num <= countLimit:
        
        returnedString = recursivePrint(num)
    
        #past here means we have reached the bottom and are moving back up
            
        #initialize the temp string for each function call
        tempString = ""
        thisString = ""
        
        if num % 3 == 0:
            thisString += "\nFizz"
        if num % 5 == 0:
            if num % 3 == 0:
                thisString += "Buzz"
            if num % 3 != 0:
                thisString += "\nBuzz"
        if num % 3 != 0 and num % 5 != 0: thisString += ('\n' + str(num))
        
        
        tempString = thisString
        
        #check for empty returnString on first run through
        if returnedString: tempString += returnedString
        
        #pass the string back up to be added onto
        return tempString
    
if method == "ifelse": ifElseMethod(count)
elif method == "concat": stringConCatMethod(count)
elif method == "recursive": recursiveMethod()
else: print("No function found")


    
    
    
