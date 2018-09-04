# functions in python

# all the functions begin with a 'def' + 'name' + '():'
# and inside the function, code begin after a TAB
def say_hi():
    print("Hi")
    print("all the functions begin with a 'def' + 'name' + '():'\n" +
          "and inside the function, code begin after a TAB")

# call the function
say_hi()


# functions with parameter
def say_hi_to(input_name):
    print("Hi " + input_name)

say_hi_to("Fang")


# function with a return value
def cube(num):
    return num*num*num

print(cube(6))
