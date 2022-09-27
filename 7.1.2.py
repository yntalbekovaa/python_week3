import numpy

def sumNMean(arr):
    list_new = list(map(int, arr.split()))
    sum1 = sum(list_new)
    mean = numpy.mean(list_new)
    print("array",list_new,",sum of elements:",sum1,".Mean :",mean)


n = int(input("Enter the number of arrays:"))

arrList = []
for i in range(n):
    arrList.append(input("Enter the array :"))

for i in range(n):
    sumNMean(arrList[i])
