mylist1 = [1, 2, 3]
mylist2 = ["a", "b", "c"]
mylist3 = [100, 200, 300]


for index, element in enumerate(mylist2):
    print(index, element)

for element in zip(mylist1, mylist2, mylist3):
    print(element)

zipped_list = list(zip(mylist1, mylist2, mylist3))
print(zipped_list)
