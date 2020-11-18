import math

current_x = abs(int(input("Current X coordinate: ")))
current_z = abs(int(input("Current Z coordinate: ")))

dest_x = abs(int(input("Destination X coordinate: ")))
dest_z = abs(int(input("Destination Z coordinate: ")))

dist_x = abs(dest_x - current_x)
dist_z = abs(dest_z - current_z)

dist_x_sqd = dist_x ** 2 
dist_z_sqd = dist_z ** 2

dist_sqd = dist_x_sqd + dist_z_sqd
distance = math.sqrt(dist_sqd)
output = distance / 20160

print(output)
# Blocks Per Hour: 20,160
# distance/20,160 = 6