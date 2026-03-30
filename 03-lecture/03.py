
# Define the traffic light color
traffic_light = "Green"

# Define whether the road is clear
road_clear = True

# Checking the traffic conditions
if traffic_light == "Green":
    # Nested condition: Checking if the road is clear
    if road_clear:
        print("You can GO! The road is clear.")
    else:
        print("Wait! The road is not clear, even though the light is green.")
elif traffic_light == "Yellow":
    print("Slow down and PREPARE TO STOP! ")
else:
    print("You must STOP! ")