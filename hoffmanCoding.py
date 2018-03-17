import __future__
from collections import Counter
import time

string = "Hello world!"

#binCharList = [] 
#charDict = {}


class Tree:
    def __init__(self, cargo, count, left=None, right=None):
        self.cargo = cargo # value of this item in the tree (e.g. 'y')
        self.count = count # how many times this tree occurs (e.g. 10 times)
        self.left  = left # link to left member of the tree 
        self.right = right # link to right member of the tree below

    def __str__(self):
        return str(self.cargo)

#calculate the second smallest number in a list
def secondSmallest(treeList):
    
    # tempList = treeList
    
    # minVal = min(tempList)
    # print("min: ".format(minVal))
    

    # for entry in tempList:
    #     if entry == minVal:
    #         tempList.remove(entry)
    #         break
    
    # secondMin = min(tempList)
    
    # return secondMin

    m1, m2 = float('inf'), float('inf')
    
    #loop through all the numbers in the list
    for num in treeList:
        
        #if this number is smaller than, or equal to, m1, set num to be the new m1, and m1 to be the new m2
        if num.count <= m1:
            m2 = m1
            m1 = num
            
        
        #if num is only smaller than m2, then set num to be the new m2
        elif num.count < m2:
            m2 = num
    
    #return the two smallest numbers
    return m2    

def twoSmallest(treeList):
    smallest = min(treeList)
    
    secondSmall = secondSmallest(treeList)
    
    print("smallest number: {}, second smallest: {}".format(smallest.count,secondSmall.count))
    
    return [smallest, secondSmall]
    
def makeTree(stringToEncode):

    #return a list of how many times in `string` each character occurs {'a': 4,...}
    counter = Counter(stringToEncode)
    print counter
    
    
    tree = []
    
    
    #create the initial single-level tree
    #loop through each entry in the list of counted characters
    for key in counter.keys():
        temp = Tree(key, counter[key])
        tree.append(temp)
    
    print tree
    
    #time.sleep(10)
    
    #find the two smallest entries, and merge them (delete old entries, make one new entry)
    
    #while we have not yet merged all the entries
    while len(tree) > 1:
        
        #get two smallest entries
        twoSmall = twoSmallest(tree)
        
        tempTree = []
        
        count = 0
        
        for branch in tree:
            
            #only keep merging till you have two entries
            if count < 2:
                
                #print("branch.count: {}".format(branch.count))
                #print("twoSmall[0]: {}".format(twoSmall[0].count))
                
                #if this entry in the tree is equal to the smallest number
                if branch.count == twoSmall[0].count:
                    
                    tempTree.append(branch)
                    
                    #print("before length: {}".format(len(tree)))
                    #remove this old entry from the list
                    tree.remove(branch)
                    
                    #print("after length: {}".format(len(tree)))
                    
                    count += 1
        
        print(tempTree)
        
        #time.sleep(10)
                   
        #if there was only one entry with the smallest number (no duplicates), find the second smallest number            
        if count < 2:
            print("only found one entry to match the smallest number. Looking for entry with second smallest")
            
            for branch in tree:
            
                #only keep merging till you have two entries
                if count < 2:
                    #if this entry in the tree is equal to the second smallest number
                    if branch.count == twoSmall[1].count:
                        tempTree.append(branch)
                        
                        #remove this old entry from the list
                        tree.remove(branch)
                        
                        count += 1
                        
                        
        if count == 2:
            
            
            
            #append the new merged entries, with no cargo at this level, and a cound of the sum of the contained two elements
            tree.append(Tree(None, (tempTree[0].count+tempTree[1].count), tempTree[0], tempTree[1]))
            
            print("have both entries, new length of tree is {}".format(len(tree)))
            
        else: print("unable to find two smallest entries. Found {} elements".format(count))
        
        print("length of tree after this iteration: {}".format(len(tree)))
        
        time.sleep(3)

    time.sleep(10)
    
    #return the finished tree
    return tree



def encodeString(stringToEncode, tree):
    
    #follow the tree down to find where the letter in question is. Is there a way to just get the list of parents?
    print







#stringLen = len(string)
#print("This string takes up {} bytes when uncompressed".format(stringLen) )




# for char in string:
    
#     if charDict.get(char):
#         print("Existing entry for {}, incrementing the counter".format(char))
#         charDict[char] += 1
#     else:
#         print("No existing entry for {}, creating one...".format(char))
#         charDict[char] = 1
    
#     tempString = bin(ord(char))[2:].zfill(8)
#     print(tempString)
#     print(type(tempString))
    
    
    
    
#    binCharList.append(tempString)
    
#print(binCharList) 

#tree = sorted(charDict, key=charDict.get)

#print(tree)

#create tree starting with least common items in dict


#def count

def encode(stringToEncode):
    
    tree = makeTree(stringToEncode)
    
    encodedString = encodeString(stringToEncode, tree)


def main():
    inputString = raw_input("What string would you like to encode? ")
    
    print encode(inputString)

if __name__ == '__main__':
    main()