#Task2:and loops

#A list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

print("List of fruits:",fruits)

print("First fruit:",fruits[0])

fruits.append("orange")
print("List after adding fruit:",fruits)

fruits.remove("elderberry")
print("list after removal:",fruits)

#loop over list 
for fruit in fruits:
    print("I like",fruit)
print("Total fruits:",len(fruits))
