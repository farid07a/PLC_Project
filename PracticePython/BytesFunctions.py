
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
