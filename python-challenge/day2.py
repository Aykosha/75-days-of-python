#Task 1: Data Type Explorer. Explore types with type()

print(type("Summer")) #Output: <class 'str'>
print(type(500)) #Output: <class 'int'>
print(type(3.5)) #Output: <class 'float'>
print(type([1, 2, 3, 4])) #Output: <class 'list'>

#Task 2: Personal Bio Generator

name = input("Your name: ") or "Anonymous"
age = int(input("Your age: "))
hobby = input("Your hobby: ")
fun_fact = input("Fan fact about you: ")

#Combine into a bio using f-strings
print(f"Meet {name}, a {age}-year-old who loves {hobby}")
print(f"Fan fact: {fun_fact}")

#Day 2 Motivation:
print("Consistency compounds—you’re already ahead of yesterday’s you! 💪")
