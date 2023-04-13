import os
os.system('clear')
p = 1
q = int(input("Enter b:"))
i = int(input("enter n:"))

while i > 0:
    if (i%2) == 1:
        p = p * q
    q = q * q
    i = i // 2      
print(p)




