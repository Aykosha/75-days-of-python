#Task: User profile builder

profile = {} #Create dic

#Collect user data
profile["name"] = input("Your name: ")
profile["age"] = int(input("Your age: "))
profile["skills"] = input("Your skills (comma-separated): ").split(",")

#Dynamic output
print("\nProfile Summary:")
for key, value in profile.items():
    print(f"{key.capitalize()}: {value}")
