### MASTER YODA: Given a sentence, return a sentence with the words reversed


def master_yoda(text):
    result = ""
    words = text.split()
    words = words[::-1]
    result = " ".join(words)
    return result


print(master_yoda('I am home'))


################
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
################

def has_33(nums):
    counter = 0
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


print(has_33([1, 3, 4, 3, 3]))


###################
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
###################

def paper_doll(text):
    result = ''
    for letter in text:
        result += letter * 3
    return result


print(paper_doll("Hhello"))


####################
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    result = a + b + c
    if result <= 21:
        return result
    elif result <= 31 and 11 in (a, b, c):
        return result - 10
    else:
        return "BUST"


print(blackjack(10, 9, 9))


#  SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


# Check
spy_game([1, 2, 4, 0, 0, 7, 5])
