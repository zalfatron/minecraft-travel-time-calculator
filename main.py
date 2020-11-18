import math

# Find the coordinates that the player is currently at
current_x = abs(int(input("Current X coordinate: ")))
current_z = abs(int(input("Current Z coordinate: ")))

# Find the coordinates that the player wants to go to
dest_x = abs(int(input("Destination X coordinate: ")))
dest_z = abs(int(input("Destination Z coordinate: ")))

# Find the length of side A and B
dist_x = abs(dest_x - current_x)
dist_z = abs(dest_z - current_z)

# Square sides A and B
dist_x_sqd = dist_x ** 2 
dist_z_sqd = dist_z ** 2

# Add the squared side A and side B
dist_sqd = dist_x_sqd + dist_z_sqd

# Finds the distance between the two sets of coordinates given
distance = math.sqrt(dist_sqd)

# Calculats how long it will take to travel the specified distance
output = distance / 20160

# Prints the estimated travel time
print("You're journey will take " + output + "hours")

# Blocks Per Hour: 20,160
# distance/20,160 = 6
