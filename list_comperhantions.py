mystring = 'hello'

mylist = []
for letter in mystring:
    mylist.append(letter)


mylist2 = [letter for letter in mystring]

mylist3 = [num**2 for num in range(11)]

mylist4 = [x for x in range(11) if x % 2 == 0]

print(mylist)
print(mylist2)
print(mylist3)
print(mylist4)


celsius = [0, 10, 20, 34.5, 36.6]

fahrenheit = [((9/5) * c_temp + 32) for c_temp in celsius]

print(fahrenheit)


celsius2 = []
for f_temp in fahrenheit:
    celsius2.append((f_temp - 32) * (5/9))

print(celsius2)


### if else in list comperhantion

result = [x if x % 2 == 0 else "odd" for x in range(11)]
print(result)


### nested loop


numbers1 = [1, 2, 3]
numbers2 = [100, 400, 700]
nested = [x * y for x in numbers1 for y in numbers2]
print(nested)
