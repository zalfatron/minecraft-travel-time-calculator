current_x_cord = abs(int(input("Current X coordinate: ")))
current_z_cord = abs(int(input("Current Z coordinate: ")))

destination_x_cord = abs(int(input("Destination X coordinate")))
destination_z_cord = abs(int(input("Destination Z coordinate")))

distance_x = destination_x_cord - current_x_cord
distance_z = destination_z_cord - current_z_cord

print(distance_x)
print(distance_z)

# Blocks Per Hour: 20,160