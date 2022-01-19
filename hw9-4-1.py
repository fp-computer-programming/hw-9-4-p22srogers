# Author: SMR (AMDG) 1/18/22
def smash(lst):
    x = ""
    for index, value in enumerate(lst):
        if index == 0:
            x = x + value
        else:
            x = x +" "+ value
    return x
print(smash(["Buy", "the", "dip."]))