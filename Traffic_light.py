t_lights = input("What colour are the traffic lights? (red, yellow or green) : ").lower()
# The above line of code allows you to input values/characters after the printed output.
# the .lower prints whatever is inputted in lower case.

if t_lights == "red":
    print("Stop")
#     the above statement is an if statement and says that if the input is the same as the string red, it will print out stop
elif t_lights == "yellow":
    print("Get ready to stop")
    #     the above statement is an elif statement and checks multiple conditions sequentially
#     elif allows you to specify additional conditions if the previous "if" statement is false
# here it will print "get ready to stop" if the input written was "yellow"
elif t_lights == "green":
    print("Go.")

else:
    print("Try again. Enter either: red, yellow, or green.")
    # if none of the elif or if conditions are met, then the else statement will run.