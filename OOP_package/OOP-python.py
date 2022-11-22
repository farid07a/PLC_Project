x = False
x= "codezila"
print(type(x))

print(x.upper())

print("Concatenate "+"Islam")


for letter in "hello":
    print(letter)

liName=["farid", "karim", "bormal"]

for name in liName:
    print(name)

for i in range(20): # 0-9
    print(i)

print("------------")
for i in range(10,20): # 10-19
    print(i)

stringname="hello world"

for i in range(len(stringname)):
    print(stringname[i])


print(2**3)

# -------- 2D list

list2d=[
    [1,2,3],
    [3,4,5],
    [6,7,8],
    [12]

        ]

print(list2d)

print(list2d[0])

print(list2d[3][0])

for row in list2d:
    for v in row:
        print(v)