current_x = abs(int(input("Current X coordinate: ")))
current_z = abs(int(input("Current Z coordinate: ")))

dest_x = abs(int(input("Destination X coordinate")))
dest_z = abs(int(input("Destination Z coordinate")))

distance_x = abs(dest_x - current_x)
distance_z = abs(dest_z - current_z)

print(distance_x)
print(distance_z)

# Blocks Per Hour: 20,160
# distance/20,160 = 6