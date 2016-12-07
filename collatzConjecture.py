num = 1
steps = []

while num < 20:
    temp = num
    count = 0
    while temp != 1:
        if temp %2 == 0:
            temp = temp/2
            count += 1
        else:
            temp = (temp *3) + 1
            count += 1
        
    print 'For the number ' + str(num) + ' it took ' + str(count) + ' steps'
    steps.append([num, count])
    num += 1

print steps