prime_numbers = [2, 3, 5, 7]
# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)
print(len(byte_array))
# ------------------------------------------------
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(len(arr))
# -------------------------------------------------
size = 5
arr = bytearray(size)
print(len(arr))
# -------------------------------------------------
# declaring an integer value
integer_val = 5

# converting int to bytes with length
# of the array as 2 and byter order as big
bytes_val = integer_val.to_bytes(2, 'big')

# printing integer in byte representation
print(bytes_val)
# -------------------------------------------------
# declaring an integer value
integer_val = 10

# converting int to bytes with length
# of the array as 5 and byter order as
# little
bytes_val = integer_val.to_bytes(5, 'little')

# printing integer in byte representation
print(bytes_val)
# ------------------------------------------------
# declaring an integer value
int_val = 5

# converting to string
str_val = str(int_val)

# converting string to bytes
byte_val = str_val.encode()
print(byte_val)
# -----------------------------------------------


