# In python, you don't need to declare the type of the variable. Python will check the type
sName = "John"
iAge = 35
# the first letter for true and false in boolean for python need to be capitalise
is_male = True
is_male = False

# You can use  '+' to connect two strings together.
#  ** However, you cannot use '+' to connect non-string variable in 'print()'
print(" ** You cannot use '+' to connect non-string variable in 'print()' ")

# ** so you need to use 'str([int-variable])' or [int-variable].__str__()
print(" ** so you need to use 'str([int-variable])' or [int-variable].__str__() ")

print(sName + " is " + str(iAge) + " old.")
print(sName + " is " + iAge.__str__() + " old.")
