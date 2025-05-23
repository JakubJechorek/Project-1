# In this exercise, you are tasked to create a Python program that simulates a package loading system.
# Each package can carry a maximum of 20 kg of goods.
# Items are added to the package with weights ranging from 1 to 10 kg.
# If adding an item to the package would exceed the 20 kg limit, the package should be sent,
# and the current item should start a new package.
# If an item with a weight of 0 is given, the program should terminate.
#
# 1. Write a program that prompts the user for the maximum number of items to be shipped.
# 2. The program should allow the user to enter the weight of each item, one by one.
# 3. If adding an item would increase the total weight of the current package above 20 kg,
# mark the current package as sent and start a new package with the current item.
# 4. If an item with a weight of 0 kg is given,
# the program should terminate as if the maximum number of items has been reached.
# 5. At the end of the program, display the following information:
#
#       Number of packages sent
#       Total weight of packages sent
#       Total 'unused' capacity (non-optimal packaging).
#       This is calculated as the number of packages sent multiplied by 20 kg, minus the total weight of packages sent.
#       The package number that had the most 'unused' capacity and the amount of 'unused' capacity in that package.
#
#
# Hints:
#
# - Use a loop to continuously prompt the user for item weights until the maximum number of items has been reached or an item with a weight of 0 kg is given.
# - Keep track of the current package's total weight and the number of packages sent.
# - Remember to handle cases where the weight of an item is outside the acceptable range (1 to 10 kg, unless it's 0).
# - Handle user inputs that are not as expected (for example, if the user enters a string instead of a number for the item('s weight). '
# 'The program should not crash in these cases, but instead, it should display an appropriate error message.)


MAX_PACKAGE_WEIGHT = 20
MIN_ITEM_WEIGHT = 1
MAX_ITEM_WEIGHT = 10

while True:
    try:
        max_items = int(input("Enter the maximum number of items to be shipped: "))
        if max_items <= 0:
            print("Please Enter a positive number.")
            continue
        break
    except ValueError:
        print("invalid input. Please enter a number.")

item_count = 0
package_count = 0
total_weight = 0
current_package_weight = 0
unused_capacities = []

while item_count < max_items:
    try:
        weight_input = input(f"enter weight of item #{item_count + 1} (Between 1-10 KB, 0 to finish): ")
        item_weight = int(weight_input)

        if item_weight == 0:
            print("Weight of 0 detected, Terminating input.")
            break

        if item_weight < MIN_ITEM_WEIGHT or item_weight > MAX_ITEM_WEIGHT:
            print("Invalid Weight, The weight must be between 1 and 10 KGs.")
            continue

        if current_package_weight + item_weight > MAX_PACKAGE_WEIGHT:
            # sending the current package
            package_count += 1
            unused_capacity = MAX_PACKAGE_WEIGHT - current_package_weight
            unused_capacities.append(unused_capacity)
            total_weight += current_package_weight
            print(f"package #{package_count} sent with weight {current_package_weight} KG.")

            # starting new package with current item
            current_package_weight = item_weight
        else:
            current_package_weight += item_weight

        item_count += 1

    except ValueError:
        print("Invalid input. Please enter number.")

# sending the final package if there is any item.
if current_package_weight > 0:
    package_count += 1
    unused_capacity = MAX_PACKAGE_WEIGHT - current_package_weight
    unused_capacities.append(unused_capacity)
    total_weight += current_package_weight
    print(f"Package #{package_count} sent with weight {current_package_weight} KG.")

# Final Statistics
total_unused_capacity = package_count * MAX_PACKAGE_WEIGHT - total_weight
max_unused_capacity = max(unused_capacities, default=0)
package_with_max_unused = unused_capacities.index(max_unused_capacity) + 1 if unused_capacities else 0

print("\nSummary:")
print(f"Number of packages sent: {package_count}")
print(f"Total weight of packages sent: {total_weight} kg")
print(f"Total unused capacity: {total_unused_capacity} kg")
if package_with_max_unused > 0:
    print(f"Package with most unused capacity: Package #{package_with_max_unused} ({max_unused_capacity} kg)")
else:
    print("No packages were sent.")
