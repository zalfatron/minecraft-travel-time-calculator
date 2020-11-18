# ERROR on lines 2,3,5,6: bad operand type for abs(): 'str'
current_x_cord = str(abs(int(input("Current X coordinate: "))))
current_z_cord = str(abs(int(input("Current Z coordinate: "))))

destination_x_cord = str(abs(int(input("Destination X coordinate"))))
destination_z_cord = str(abs(int(input("Destination Z coordinate"))))

distance_x = destination_x_cord - current_x_cord
distance_z = destination_z_cord - current_z_cord

print(distance_x)
print(distance_z)

# Blocks Per Hour: 20,160