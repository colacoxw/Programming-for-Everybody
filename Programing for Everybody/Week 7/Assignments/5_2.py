largest = None
smallest = None
values = [7, 2, 'bob', 10, 4]
index = 0

while index < len(values):
    value = values[index]
    if isinstance(value, int):  # Check if the value is an integer
        if largest is None or value > largest:
            largest = value
        if smallest is None or value < smallest:
            smallest = value
    else:
        print('Invalid input')
    index += 1

print("Maximum is", largest)
print("Minimum is", smallest)