# Let's experiment with functions now, shall we?  A function is some code that
# is saved and given a name to be used later on in the code, usually more than
# once.  In Python, functions are defined using the "def" keyword.  Let's make
# a function that takes anything as the input, and prints it using the "print"
# function.

def say(what_to_say): # "say" is what our function will be named.
    # The "(what_to_say)", means that the function will take one parameter as
    # the input, and then that input will be turned into the "what_to_say"
    # variable.
    
    print(what_to_say)

# In our function, we simply made a small amount of code that basically
# replaces the "print" function with the "say" function.  Now we can test out
# our new function!

say("Hello World")

say(1 + 2)

x = 4
y = 3
say(x + y)

# These tests are all based on our previous lessons.  The "say" function can
# now be used instead of the "print" function, but only in this file, because
# the function isn't automatically copied to other files.
