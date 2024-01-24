myList = ["milk", "apples", "oranges", "potatoes", "bread"]
myList.append("bananas")
myList.insert(1, "onions")

print(myList)

myList.remove("potatoes")

print(myList)

myList = [("milk", "dairy"), ("onions", "fruits"), ("apples", "fruits"),
            ("oranges", "fruits"), ("bread", "bakery"), ("bananas", "fruits")]
print(myList)

for item, section  in myList:
    print(f"You can find {item} in {section} section.")

myList = {"milk":"dairy", "onions":"fruits", "apples":"fruits",
          "oranges":"fruits", "bread":"bakery", "bananas":"fruits"}

print(myList.keys())
print(myList.values())
print(myList.items())