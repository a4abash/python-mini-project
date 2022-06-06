list=[1,22,7,98,45,17,8,2,75,103,63,33,39]

list.sort() #sorts list in ascending order
number = int(input("Enter the number you want to check"))    # 98

#[1, 2,  7,  8,  17, 22, 33, 39, 45, 63, 75, 98, 103]
#(0  1   2   3   4   5   6   7   8   9   10  11  12

def binarySearch(target,output):
    while output == -1:
        midpoint = int(len(list)/2) # length of the list and midpoint

        if list[midpoint] == target: # conditon to check if target matched
            print("Matched",list[midpoint], 'was found on the list')
            break

        elif list[midpoint]<target:
            if midpoint==0:
                print(target,'was not found on the list')
                break
            for i in list[:midpoint]:
                list.remove(i)
            print(list)
            
        else:
            if midpoint ==0:
                print('Not found')
                break
            for i in list[midpoint:]:
                list.remove(i)
            print(list)
            
if __name__ == '__main__':
    binarySearch(number,output=-1)
