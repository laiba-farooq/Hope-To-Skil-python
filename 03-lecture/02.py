car_speed = 60

# Define whether the driver is wearing a seatbelt
seatbelt_on = False

# Check if the driver is following traffic rules
if car_speed <= 60:  # Speed limit check
    if seatbelt_on:  # Seatbelt check
        print("You are driving safely! ")
    else:
        print("Warning! Please wear your seatbelt. ")
else:
    print("Slow down! You are exceeding the speed limit! ")