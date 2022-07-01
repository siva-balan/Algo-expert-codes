from re import X


def binarysearch(left,right,num,target):
    while left<= right:
        middle = (left + right) // 2
        midvalue = num[middle]
        if (midvalue > target):
            right = middle -1
        elif (midvalue < target):
            left = middle + 1
        elif target == midvalue:
            return middle
    
    
n = int(input("no of array elements:"))

num = []
print("enter the array elements in sorted order")
for i in range(0,n):
    x = int(input())
    num.append(x)

target = int(input("number to be found:"))
print(binarysearch(0,n-1,num,target))
