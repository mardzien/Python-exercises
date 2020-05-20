# print words that start with s in this sentense
st = "Print only words that start with s in this sentence"
###
words = st.split()
for word in words:
    if word[0] == 's':
        print(word)


# use list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

mylist = [x for x in range(1, 51) if x % 3 == 0]
print(mylist)

# print words with even length
st = "Print only words in this sentence that has an even number of letters"
words = st.split()
for word in words:
    if len(word) % 2 == 0:
        print(word)


### Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz"
# instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
