# Author: SMR (AMDG) 1/18/22
def count_e(number):
    x = 0
    for letter in number:
        if letter == "e":
           x += 1
    return x
print(count_e("cryptocurrency"))