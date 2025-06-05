#Task: Grocery list manager

grocery = [] #Empty list
while True:
    item = input("Add grocery item (or 'done'): ")
    if item == "done":
        break
    grocery.append(item)

print ("\nYour Grocery List:")
for item in grocery:
    print(f"- {item}")
