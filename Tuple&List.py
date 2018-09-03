# get input from user

# ** variable type: "tuple", hard code only, once you set it, you cannot change it (Read Only)
coordinates = (4, 5)
# tuple: coordinates = (4, 5)
# list:  coordinates[4, 5]
# list of tuple: coordinates[(1,2),(4,5),(45,68)]

# if you try to change it you will get error
# coordinates[0] = 20
print("if you try to change it you will get error:\n  "
      "TypeError: 'tuple' object does not support item assignment")

# you can read it by:
print(coordinates[1])
