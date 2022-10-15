
tuple_obj=(14,12,36,15)  # (,) is Tuples No add No change No delete Imutable
                         # Used In fix List (like Days, Month
print("Tuple : ",tuple_obj)

for numTuple in tuple_obj:
    print(numTuple)

# list Mutable Can Add Can Change Can delete

list_obj=[20,63,78,1,0]
print("Dynamic List :",list_obj)

for numList in list_obj:
    print(numList)

# Add In list
list_obj.append(100)
print(list_obj)
list_obj.insert(3, 150) # insert in case Number 4 And Shifft other Case
print(list_obj)

# Manipulate String Like List

String_as_list = "Muhammed"

print("character :",String_as_list[2]) # Character in index 2
Start_by_index_to_end = String_as_list[3:]
print(Start_by_index_to_end)  # -> ammed
Start_by_Firstindex_to_LastIndex_1=String_as_list[3:5]
print(Start_by_Firstindex_to_LastIndex_1)  # ha (3,4) index

for ch in String_as_list:
    print(ch)
