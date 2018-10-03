print("Welcome to our shop, what do you want")
items = ["T-shirt", "Sweater"]
print(items)
newitem = input("Enter new item ")
items.append(newitem)
print(items)


n = int(input("Update position ? "))
while True:
    if n >2 or n<-3:
        print("Enter again")
        break
    else:
        print(items[n-1])
        break

m = input("New item ? ")
items[n-1] = m
print(items)

d = int(input("Delete position ? "))
while True:
    if d >2 or d <-3:
        print("Enter again")
        break
    else:
        print(items[n-1])
        break
print(items[d])
print(items)