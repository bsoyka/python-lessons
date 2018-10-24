# Programs are great when they don't need any help from humans, but what if
# you want to get some information from the person running the program?  We
# can do this using the built-in "input" function.  This function will
# normally take one parameter, and that is the promopt to show the user.

x = input("Enter your name: ")
print("Hello, " + x)

# Also, notice how we used a "+" to put "Hello, " and the user's name
# together.  This is called concatentation, and it is when you combine two
# strings.  Now, what if there's ever an error that happens often in a
# specific part of your code?  You can use what is called a try-except
# statement to help with that.  The way a try-except statement works, is it
# will try the code in the "try" section, and if there's an error, it will
# stop running the "try" code, and it will begin running the "except" code
# instead.

try:
    x = input("Enter a number: ")
    print(x + 1)
except:
    print("Error")

# Using a try-except statement means that when a well-known error occurs, your
# program can keep running as long as you have planned for the error.  Now,
# why did this code have an error?  This is the input function returns a
# string, so Python assumed you wanted to concatenate two strings.  You can
# only concatenate strings, not integers, so you can't add/concatenate a
# string (the input) + an integer (the 1).  What if we wanted to get a number
# from the user, and then use it in our program?

try:
    x = input("Enter a number: ")
    y = int(x)
    print(y + 1)
except:
    print("Error")

# Great!  Now our program functions properly.
