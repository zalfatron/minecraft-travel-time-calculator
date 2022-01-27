import math as m

# Find the coordinates that the player is currently at
current_x = int(input("Current X coordinate: "))
current_z = int(input("Current Z coordinate: "))

# Find the coordinates that the player wants to go to
dest_x = int(input("Destination X coordinate: "))
dest_z = int(input("Destination Z coordinate: "))

# Calculate the distance
distance = m.sqrt((dest_x - current_x) ** 2 + (dest_z - current_z))

# Calculats how long it will take to travel the specified distance
output = str(distance / 20160)

# Prints the estimated travel time
print("Your journey will take " + output + " hours.")

# Blocks Per Hour: 20,160
# distance/20,160 = output
