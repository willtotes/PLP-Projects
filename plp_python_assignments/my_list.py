
my_list = []
print(f"Empty list: {my_list}")

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"Appending 10-40: {my_list}")

my_list.append(15)
print(f"Inserting the value of 15: {my_list}")

my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(f"Extending my_list: {my_list}")

my_list.remove(70)
print(f"Removing the last element: {my_list}")

my_list.sort()
print(f"Sorting my_list: {my_list}")

index_of_thirty = my_list.index(30)
print(f"The index of 30: {index_of_thirty}")


