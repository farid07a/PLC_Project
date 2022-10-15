
num=0

while num<30:
    print("Num:",num)
    num+=1
print("Num After while loop :", num)

num=0
while num<30:
    print("Num:",num)
    num += 5

print("Num After while loop :", num)

myFile = open('MuhammedEssa\\pp.txt')

for i,txt in enumerate(myFile):
    print(i,txt)
