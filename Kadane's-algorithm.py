def maxSubarr(n,num):

    maxhere, totalmax = num[0],num[0]

    for i in range(1,n):
        maxhere = max(maxhere+num[i],num[i])
        totalmax = max(totalmax,maxhere)
    return totalmax

n = int(input())
num =[]
for i in range(n):
    z =int(input())
    num.append(z)

y = maxSubarr(n,num)
print(y)
