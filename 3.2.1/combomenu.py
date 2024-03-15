sandwich_type = ""
subtotal = 0.0

order_list = []

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwich_type = input("Sandwich Choice: ")

# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
    order_list.append ("chicken")
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
    order_list.append ("tofu")
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25
    order_list.append ("beef")

# Beverage Choice
bev_choice = input("Do you want a beverage? yes or no")
if bev_choice == "yes":
    bev_size = input("What size beverage would you like? Small, Medium, or Large")
    if bev_size == "small":
        print("You chose small, so $1.00")
        subtotal += 1
        order_list.append("small")
    if bev_size == "medium":
        print("You chose medium, so $1.75")
        subtotal += 1.75
        order_list.append("medium")
    if bev_size == "large":
        print("You chose large, so $2.25")
        subtotal += 2.25
        order_list.append("large")

# Fries
fry_choice = input("Do you want french fries? Yes or No")
if fry_choice == "yes":
    fry_size = input("What size fries would you like? Small, Medium, or Large")
    if fry_size == "small":
        supersize = input("Do you want to supersize that for $2? Yes or no")
        if supersize == "yes":
            fry_size = "large"
            subtotal += 2
            order_list.append("Large")
        else:
            print("You chose small fries for $1")
            subtotal += 1
            order_list.append("Small")
    elif fry_size == "medium":
        print("You chose medium for $1.50")
        subtotal += 1.50
        order_list.append("Medium")
    else:
        print("You chose large fries for $2")
        subtotal += 2
        order_list.append("Large")

# Ketchup
ketchup = float(input("How many ketchup packets would you like? $0.25 each"))
if ketchup >= 0:
    subtotal += ketchup * .25
    order_list.append(ketchup)

if bev_choice == "yes" and fry_choice == "yes":
    subtotal -= 1

print(sandwich_type)
if bev_choice == "yes":
    print(bev_size)
if fry_choice == "yes":
    print(fry_size)

print("")
print(subtotal)
print(order_list)