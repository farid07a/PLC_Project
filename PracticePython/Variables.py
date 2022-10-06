
x = y = z = 10

print('x=', x)
print("y=", y)
print("z=", z)


String_Var = "String Class"

print("Type x:", type(x))
print("Type String :", type(String_Var))

# Lists Dynamic array
# Tuples Static array Not changeable
# مصفوفات ليس لها حجم ثابت, و لا يمكن حذف قيمها, و يمكن إضافة قيم جديدة فيها يقال لها Sets..
# جداول تخزن البيانات فيها بطريقة مفايتح (Keys) و قيم (Values) يقال لها Dictionaries.

#   String Variable

# هنا قمنا بتعريف ثلاث متغيرات تحتوي على قيم نصية
name = 'Mhamad'
job = "Programmer"
message = '''This string that will span across multiple lines. No need to use newline characters for the next lines.
The end of lines within this string is counted as a newline when printed.'''
# هنا قمنا بعرض قيم المتغيرات النصية بأسلوب مرتب
print('Name: ', name)
print('Job: ', job)
print('Message: ', message)

# True و قيمته check هنا قمنا بتعريف إسمه
check = True
# True تساوي check سيتم تنفيذ أمر الطباعة الموضوع هنا إذا كانت قيمة المتغير
if check == True:  # we can write if check == 1 or if check:
    print('check = True')
# False أي إذا كانت تساوي True تساوي check سيتم تنفيذ أمر الطباعة الموضوع هنا إذا لم تكن قيمة المتغير
else:
    print('check = False')

# تخزين البيانات في List

A = []                                 # هنا قمنا بتعريف مصفوفة فارغة
B = [10, 20, 30, 40, 50]               # هنا قمنا بتعريف مصفوفة تحتوي على أعداد صحيحة فقط
C = ['Mhamad', 'Samer', 'Abdullah']    # هنا قمنا بتعريف مصفوفة تحتوي على نصوص فقط
D = [1, 'two', 'three', 4]             # هنا قمنا بتعريف مصفوفة تحتوي على أعداد صحيحة و نصوص

# هنا قمنا بتعريف مصفوفة من النصوص تتألف من 4 عناصر
listNames = [str] * 4

listNames[0] = "khaled ben ramdan"
listNames[1] = "rachid othman"
listNames[2] = "dibouche"
listNames[3] = "farid"
listNames.append("ishak")

# هنا قمنا بإضافة عنصر جديد على المصفوفة
listNames.append('karim')
# هنا قمنا بعرض قيم المصفوفة و عدد عناصرها
print('Stored languages:', listNames)
print('Number of stored languages is:', len(listNames))
# تخزين البيانات في Tuple

A = ()                                 # هنا قمنا بتعريف مصفوفة فارغة
B = (10, 20, 30, 40, 50)               # هنا قمنا بتعريف مصفوفة تحتوي على أعداد صحيحة فقط
C = ('Mhamad', 'Samer', 'Abdullah')    # هنا قمنا بتعريف مصفوفة تحتوي على نصوص فقط
D = (1, 'two', 'three', 4)             # هنا قمنا بتعريف مصفوفة تحتوي على أعداد صحيحة و نصوص

print("Tuples",B)

# هنا قمنا بتعريف مصفوفة ليس لها نوع محدد و تتألف من 4 عناصر
languages = ('Arabic', 'French', 'English', 'Spanish')

# هنا قمنا بعرض قيم المصفوفة و عدد عناصرها
print('Stored languages:', languages)
print('Number of stored languages is:', len(languages))

# تخزين البيانات في Dictionary
# يتألف من 5 عناصر dictionary هنا قمنا بتعريف
dictionary = {
    1: 'One',
    2: 'Tow',
    3: 'Three',
    4: 'Four',
    5: 'Five'
}

# هنا قمنا بعرض قيمة العنصر الذي يحمل المفتاح رقم 3
print(dictionary[3])


# هنا قمنا بتعريف مصفوفة تتألف من 5 عناصر عبارة عن أرقام صحيحة
numbers = [1, 2, 3, 4, 5]
# y و x هنا قمنا بتعريف متغيران
x = 3
y = 8
# سيتم تنفيذ أمر الطباعة x لا تحتوي على قيمة المتغير numbers إذا كانت المصفوفة
if x not in numbers:
    print('x value not exists in the array')
# سيتم تنفيذ أمر الطباعة y لا تحتوي على قيمة المتغير numbers إذا كانت المصفوفة
if y not in numbers:
    print('y value not exists in the array')
if x in numbers:
    print('x value exists in the array')