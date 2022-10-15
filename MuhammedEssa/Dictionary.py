# dictionary Is Immutable class
my_dic={
    "Key" : "Value",
    "m":"muhammed",
    "s":"samir",
    "f":"farid"
}

print(my_dic)

for key in my_dic:
    print(key, my_dic[key])

dic_nums={1:100,2:200,3:300}

print(dic_nums)

dic_num_string={1:"farid",2:"hafed",3:"lamine"}
print(dic_num_string)
# Sorted Dictionary

unsorted_dictionary={3:"farid",1:"hafed",2:"lamine"}
print(unsorted_dictionary) # farid hafed lamine No sorted by keys

# use for loop to be sorted the dictionary
for key in sorted(unsorted_dictionary.keys()):
    print(key,unsorted_dictionary[key])