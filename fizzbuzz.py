import sys

count = 1
countLimit = 100
fBMethod = "ifelse"

if sys.argv[1]:
    fBMethod = sys.argv[1]

def ifElseMethod(num):
    #using if else statements
    #print("using the ifelse method")
    
    if num % 3 == 0:
        if num % 5 == 0:
            #if the number is a multiple of both 3 and 5
            print("FizzBuzz")
        #if the number is only a multiple of 3
        else: print("Fizz")
    #if the number wasn't a multiple of 3 but is a multiple of 5
    elif num % 3 == 0:
        print ("Buzz")
    #if the number is neither a multiple of 3 or 5
    else: print(num)

def stringConCatMethod(num):
    #check each criteria, concatonate onto end of string 
    #print("using the concat method")
    
    string = ""
    
    if num % 3 == 0:
        string += "Fizz"
    if num % 5 == 0:
        string += "Buzz"
    if num % 3 != 0 and num % 5 != 0: string += str(num)
    
    print(string)

def selectFBMethod(num, fBMethod):
    if fBMethod == "ifelse": ifElseMethod(num)
    elif fBMethod == "concat": stringConCatMethod(num)
    else: print("No function found")

while count <= countLimit:
    #print("Number: ", count)
    #print(fBMethod)
    #select method to check for FizzBuzz
    selectFBMethod(count, fBMethod)
    
    count += 1
    
