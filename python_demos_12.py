# run as is then change j to 12
# use the debugger to show the i counter increasing
i = 1
j = 12
while i < 42:
    # while loops run as long as the condition is true and the condition is checked  before each iteration.
    # while loops determines when to stop iterating
    i = i * 2
    # the above line shows that i is doubled after going through the cycle each time till it is larger than the value of J (12) --
    # --or whatever number you add at line 4
    if i > j:
     break
#  break is used to "break" and exit from the loop when i > j therefore stopping the cycle
#  if break is not reached, else will print ( loop expired) but is break is reached the "else" will be skipped (loop expired) and --
    #  ---"final value" will be printed
# can only be nested for a while loop, not in a function or class definition within that loop

# the else lines will print if the "break" statement is not reached
    else :
     print("Loop expired: ", i)

# if the break statement is reached then the below will print
print("Final value: ", i)

# Debugging pauses execution at breakpoints (lines you want to inspect).
# Lets you step through the code line by line.
# Shows variable values in real time.
# Allows modifying variables on the fly to test different scenarios.
# Identifies errors and exceptions with detailed messages.