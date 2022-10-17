import random
rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)


arr2 = bytearray(15)

print("arr1", arr)

print("arr2", arr2)

arr2.append(60)
print(arr2)


arr2[3] = 20

print("arr2 after change", arr2)

print(arr2[3])


a=bytearray(b'\x00\x00\x00\x01')

tw=a[0:2]
print("Two Byte extract :", tw)

b= bytearray(b'\x00\x00\x00\x02')
a[0:0] = b
# a=ba



z = 1234
tupByte = z.to_bytes(2, 'big')

b=bytearray(tupByte)

a[0:0]=b
print("B ARR:",b)
print(tupByte)
print(a)
print("Val 2 byte :", a[0:2])

# bytearray(b'\x00\x00\x00\x02\x00\x00\x00\x01')

print(" Int to byte :",int.from_bytes(a[0:2], "big"))

new = bytearray(10)
print("New Empty :", new)

for n in range(0, 10):
    print(n)
    new[n]=n

print("New After Filling:",new)

print()

a1=new[0:1]
print("a1",a1," -- ",int.from_bytes(a1,"big"))

rdm = bytearray(random.getrandbits(8) for i in range(10))


print(rdm)