my_set={1,2,3,3,4,4,4,4}
print("Set :",my_set)
my_set.add(5)
print("Set after adding 5 :",my_set)
set1=my_set
set2={4,5,6,7}
print("\nSet1 : ",set1)
print("Set2 : ",set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric Difference")
print(set1.symmetric_difference(set2))
