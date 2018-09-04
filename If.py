# if statement in python
is_male = False
is_tall = False

# single factor
if is_tall:
    print("you are tall")
else:
    print("hahahaha, you are short!")

# two factor with and, and second check factor checked by 'elif'
if is_tall and is_male:
    print("Hi~")
elif not(is_tall):
    print("Hi, cute little girl~")

# two factor with or
if is_tall or is_male:
    print("Hi")
else:
    print("OwO, what's this?")

