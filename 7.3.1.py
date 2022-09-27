import math
def cPow(lst):
    h1 = math.sqrt(math.pow(lst[0],2)+math.pow(lst[1],2))
    h2 = math.sqrt(math.pow(lst[2],2)+math.pow(lst[3],2))
    print("hypotenuses of 1 triangle =",h1)
    print("hypotenuses of 2 triangle =",h2)
    if h1 > h2:
        print("the hypotenus or 1st triangle largest:",h2)
    elif h1 == h2:
        print("theyre equal")
    else:
        print("the hypotenus or 2nd triangle largest:",h2)

tr=[]
print("enter the sides of triangle")
for i in range(2):
    print("for",i+1,"triangle")
    tr.append(float(input("the 1st side: ")))
    tr.append(float(input("the 2st side: ")))

cPow(tr)
