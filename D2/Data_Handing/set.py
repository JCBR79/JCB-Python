#New code for Set Operations and List De-duplications ---
print("---Set Operations---")
#Create two sets
set_a={10, 20, 30,40, 50, 50}
set_b= {40, 50, 60, 70, 80}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

#Find the Union of set_a and set_b and print the result.
#The union contains all unique elements from both sets.
union_set = set_a.union(set_b)
print(f"Union of Set A and Set B: {union_set}")

intersection_set = set_a.intersection(set_b)
print(f"Intersection of Set A and Set B: {intersection_set}")

difference_set = set_a.difference(set_b)
print(f"Difference (Set A - Set B): {difference_set}")

my_list = [1, 5, 10, 15, 20, 30, 40, 10, 15]
print(f"Original List with duplicates : {my_list}")

#convert my_list to a set to remove duplicates
#sets inherently store only unique elements
unique_elements_set = set(my_list)
print(f"List converted to set(duplicates removed): {unique_elements_set}")