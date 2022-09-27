arr = input("Enter the array: ")
list_new = list(map(str, arr.split()))
list_new.sort()
for i in range(len(list_new)):
    print(list_new[i], end=" ")
