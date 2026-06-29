
#Creating a list
List=[34,56,90,"Python",56,4.67,10,56]
#Append a new value at the end of the list
List.append(8)
#Insert a value at a specific index
List.insert(2, 22)
#Find the index of an element
print("index of 10 is",List.index(10))
#Remove an element by value
List.remove(56)
List.pop(0)
print(List)
#Reverse the list
print("After reversing:")
List.reverse()
print(List)
#Find the length of the list
print("length of list is",len(List))
#Count the occurrences of a value
print("56 appears", List.count(56)," times")
#Print list elements using a for loop
print("printing list using for loop")
for i in List:
    print(i)
# Print list elements using a while loop
print("By using while loop")
e=0
while e<len(List):
    print(List[e])
    e=e+1
