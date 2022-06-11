

# one correct but in wrong place
cond1 = "146"
cond2 = "069"
# one digit is right and it is in its place
cond3 = "342"
# two digit are right but both in wrong place
cond4 = "876"
# all digits are wrong
cond5 = "473"
# to create a 3*10 matrix to keep track of possible and impossible digits for each place
# initially it is zero
# the value inside "padlock" list is set -1 if not possible and 1 if possible throughout this code
padlock = [[0] * len(cond1) for i in range(10)]
# [
# 0=>[0,0,0]
# 1=>[0,0,0]
# 2=>[0,0,0]
# 3=>[0,0,0]
# 4=>[0,0,0]
# 5=>[0,0,0]
# 6=>[0,0,0]
# 7=>[0,0,0]
# 8=>[0,0,0]
# 9=>[0,0,0]
# ]

# modification to array based on condition type: one is correct but in wrong place
def mod_one_but_wrong(cond):
    for pos, digit in enumerate(cond):
        i = int(digit)
        for j in range(len(cond)):
            if pos == j:
                padlock[i][j] = -1
            else:
                if padlock[i][j] == -1:
                    continue
                padlock[i][j] = 1


# modification to the array based on condition type: one is correct and in right place
def mod_one_but_right(cond):
    for pos, digit in enumerate(cond):
        i = int(digit)
        if padlock[i][pos] != -1:
            padlock[i][pos] = 1
        else:
            padlock[i][pos] = -1
        for j in range(len(cond)):
            if j != pos:
                padlock[i][j] = -1


# modification to the array based on condition type: all digits are wrong
def mod_all_wrong(cond):
    for digit in cond:
        i = int(digit)
        for j in range(len(cond)):
            padlock[i][j] = -1


# modification to array based on condition type: two digits are right both in wrong places
# This is same as 1st  function
def mod_two_right(cond):
    mod_one_but_wrong(cond)

# a simple function to check if a list contains duplicates
def has_duplicates(values):
    if len(values) != len(set(values)):
        return True
    else:
        return False

#  checking  permutaion of remaining few digits
def check_permutation(digits):
    combinations = [[i, j, k] for i in digits[0] for j in digits[1] for k in digits[2]]
    non_duplicates=[]
    final=[]
    for comb in combinations:
        if not has_duplicates(comb):
            non_duplicates.append(comb)
    for item in non_duplicates:
        li = [str(i) for i in item]
        if len(set(cond1) & set(li)) != 1 or len(set(cond2) & set(li)) != 1 or len(set(cond3) & set(li)) != 1 or len(set(cond4) & set(li)) != 2:
           pass
        else:
            final.append(item)
    return final
def main():
    # reducing the possible digits for each empty space X, Y and Z by
    # eliminating according to given conditions
    mod_one_but_wrong(cond1)
    mod_one_but_wrong(cond2)
    mod_one_but_right(cond3)
    mod_two_right(cond4)
    mod_all_wrong(cond5)
    # extracting only few set of digits
    digits = [[] for i in range(len(cond1))]
    for digit, values in enumerate(padlock):
        for i, value in enumerate(values):
            if value == 1:
                digits[i].append(digit)
    finalanswer = check_permutation(digits)
    code = ""
    for ans in finalanswer:
        for i in ans:
            code = code + str(i)
    print("The three required code numbers: " + code)


if __name__ == "__main__":
    main()
