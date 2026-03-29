for i in range(10):        # Loop over numbers from 0 to 9
    if i == 3:
        print("Skipping 3")
        continue         # Skip the rest of the code in the loop when i is 3
    if i == 8:
        print("Breaking at 8")
        break            # Exit the loop entirely when i is 8
    print("Current number:", i)
else:
    # This block executes only if the loop wasn't terminated by break
    print("Loop completed without break.")