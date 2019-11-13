import sys, argparse


#function to generate FizzBuzz using nested if and else statements with prints
def ifElseMethod(countLimit):
    
    count = 1
    
    response = []
    #loop through all the numbers to be checked up to, and including the limit
    while count <= countLimit:
    
        if count % 3 == 0:
            if count % 5 == 0:
                #if the countber is a multiple of both 3 and 5
                response.append("FizzBuzz")
            #if the countber is only a multiple of 3
            else: response.append("Fizz")
        #if the countber wasn't a multiple of 3 but is a multiple of 5
        elif count % 5 == 0:
            response.append("Buzz")
        #if the countber is neither a multiple of 3 or 5
        else: response.append(count)
        
        count += 1
        
    return response

#function to generate FizzBuzz using just if statements and concatonating results for each number before printing
def stringConCatMethod(countLimit):
    
    count = 1
    
    response = []
    
    #loop through all the numbers to be checked up to, and including the limit
    while count <= countLimit:
    
        string = ""
        
        if count % 3 == 0:
            string += "Fizz"
        if count % 5 == 0:
            string += "Buzz"
        if count % 3 != 0 and count % 5 != 0: string += str(count)
        
        #print(string)
        #response.append(string + '\n')
        response.append(string)
        
        count += 1
        
    return response
    
def recursiveMethod(countLimit):
    
    #string = recursivePrint(0, countLimit)
    
    #resultList = []
    
    resultList = recursiveCheck(0, countLimit)
    
    #remove the leading "\n" to be character-accurate
    #print(string.lstrip())
    #return string.lstrip()
    return resultList
    
def recursiveCheck(num, countLimit):
    
    #count = 1
    
    num += 1
    
    returnedList = []
    
    #if this is not the last number to be checked
    if num <= countLimit:
        
        returnedList = recursiveCheck(num, countLimit)
        
        #print returnedList
    
        #past here means we have reached the bottom and are moving back up
            
        #initialize the temp string for each function call
        thisString = ""
        
        if num % 3 == 0:
            #thisString += "\nFizz"
            thisString += "Fizz"
        if num % 5 == 0:
            if num % 3 == 0:
                thisString += "Buzz"
            if num % 3 != 0:
                #thisString += "\nBuzz"
                thisString += "Buzz"
        if num % 3 != 0 and num % 5 != 0: 
            #thisString += ('\n' + str(num))
            thisString += str(num)    
            
        #print num
        #print thisString
        
        
            
        #check for empty returnString on first run through
        if returnedList:
            returnedList = [thisString] + returnedList
        else:
            returnedList = [thisString]
        
        #print returnedList
            
        #pass the string back up to be added onto
        return returnedList
    
    
def recursivePrint(num, countLimit):
    
    count = 1
    
    #returnedList = []
    
    num += 1
    
    #if this is not the last number to be checked
    if num <= countLimit:
        
        returnedList = recursivePrint(num, countLimit)
    
        #past here means we have reached the bottom and are moving back up
            
        #initialize the temp string for each function call
        tempString = ""
        thisString = ""
        
        if num % 3 == 0:
            #thisString += "\nFizz"
            thisString += "Fizz"
        if num % 5 == 0:
            if num % 3 == 0:
                thisString += "Buzz"
            if num % 3 != 0:
                #thisString += "\nBuzz"
                thisString += "Buzz"
        if num % 3 != 0 and num % 5 != 0: 
            #thisString += ('\n' + str(num))
            thisString += str(num)
        
        
        tempString = thisString
        
        #check for empty returnString on first run through
        if returnedList: 
            #tempString += returnedString
        
            returnedList.append(tempString)
        
        #pass the string back up to be added onto
        return returnedList
    
def selectMethod(method, limit):

    if method == "ifelse": return ifElseMethod(limit)
    elif method == "concat": return stringConCatMethod(limit)
    elif method == "recursive": return recursiveMethod(limit)
    else: return "No function found"
    
    

def main():
    
    #setup fallback values
    countLimit = 100
    method = "ifelse"
    
    #parse input arguments -m, method, -l, limit
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--method', help='Which FizzBuzz generation method to use')
    parser.add_argument('-l','--limit',help='How many numbers to run FizzBuzz for', type=int)
    args = parser.parse_args()
    
    if args.method: method = args.method
    if args.limit: countLimit = args.limit
    
    fizzbuzz = selectMethod(method, countLimit)
    
    for line in fizzbuzz:
        print(line)

if __name__ == '__main__':
    main()
    
    
    
