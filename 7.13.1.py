def armStrong(n):
    for num in range(1, 1000):

        order = len(str(num))

        sum = 0

        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)


n = int(input("enter the n: "))
armStrong(n)
