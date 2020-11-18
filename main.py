current_x = abs(int(input("Current X coordinate: ")))
current_z = abs(int(input("Current Z coordinate: ")))

dest_x = abs(int(input("Destination X coordinate")))
dest_z = abs(int(input("Destination Z coordinate")))

dist_x = abs(dest_x - current_x)
dist_z = abs(dest_z - current_z)

print(dist_x)
print(dist_z)

# Blocks Per Hour: 20,160
# distance/20,160 = 6