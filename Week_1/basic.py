# Interpreted Programming Language
# This is a comment. 
"""This is also a comment.
This is still inside a comment.
"""

var1 = 1
var2 = "Shiv"
boolean = False
var3 = "100"
# var4 = int(var2)
float_value = 2.8
converting_float = int(float_value)
# print(converting_float, type(converting_float))


# Strings
str1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
length_of_str1 = len(str1)
# print(str1.find("a"))
# print(str2 + "\n" +str3)
# print(f"Hi friends, the longest word is {str1}")

# List
arr = ["watermelon", "apple", "banana", "tomato", "cherry", "mango"]
arr.append("blueberry")
arr.remove("banana")
arr[1:3] = ["blackcurrant", "papaya"]
# print(arr)


sorted_fruit_list = []
# Sorting list of fruits which has letter "y" in it. 
for fruit in arr: 
    if "y" in fruit:
        sorted_fruit_list.append(fruit.capitalize())

# print(sorted_fruit_list)


# List Comphre -> ADVANCED
new_list = [fruit for fruit in arr if "y" in fruit]
# print(new_list)

arr.sort()
# print(arr)


collections1 = ["str1", "str2", "str3"]
collections2 = [1,2,3]
collections3 = [1.0, 2.0, 3.0]
collections4 = ["str1", 2, 3.0]
# print(type(collections4), collections4)

collections1.append("str4")
new_list = ["Cars", "Bikes", "Scooters"]

collections1.extend(new_list)

new_copy = collections1
print(new_copy)
