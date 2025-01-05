#WAP to find the total number of people above the age of 18
d={ "CHANDANA":18,
    "MANOJ JK":18,
    "JYOTHI":17,
    "HARISH":20,
    "MANASA":18,
    "RADHIKA":19,
    "SANTHOSH":23,
    "SANDEEP":25,}
print(d)
l=d.values()
e=[]
for i in l:
    if i>18:
        e.append(i)
n=len(e)
print('number of peoples,age above 18:-',n)