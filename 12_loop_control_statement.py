# run as is then change j to 12
# use the debugger to show the i counter increasing
i = 20
j = 120
# the while loop doubles i in each iteration
while i < 42:
    i = i * 2
    # exits the loop when i is greater than j
    if i > j:
        # the break statement is used to exit a loop early before its condition becomes false.
        # its 'friends' include continue and else.
        break
# the else block only runs if the while loop finishes naturally
else:
    print("Loop expired: ", i)

print("Final value: ", i)
