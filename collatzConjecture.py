def calculateCollatz(limit):
    num = 1
    
    #list of number and how many steps it took to get to 1
    steps = []
    
    while num <= limit:
        temp = num
        count = 0
        while temp != 1:
            if temp %2 == 0:
                temp = temp/2
                count += 1
            else:
                temp = (temp *3) + 1
                count += 1
        
        #add the number, and how many iterations it took to calculate it to the list
        steps.append([num, count])
        num += 1

    #print steps
    
    #return the list of numbers and steps
    return steps

def main():
    #ask user for input of who many numbers they would like to calculate for
    limit = input("How many numbers would you like to calculate? ")
    
    numberList = calculateCollatz(limit)
    
    for item in numberList:
        print('For the number ' + str(item[0]) + ' it took ' + str(item[1]) + ' steps')

if __name__ == '__main__':
    main()