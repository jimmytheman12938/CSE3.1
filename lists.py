string_list = ["W", "or", "l", "d!"]
int_list = [5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.0]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", string_list]
empty = []

boolean_list[0] = True
boolean_list.append(True)
boolean_list.append(False)

print(string_list)
string_list.remove("l")
print(string_list)

print(boolean_list)
boolean_list.remove(False)
print(boolean_list)

print(int_list[5])
int_list[5] = 23
print(int_list)

if "Hello" in mixed_list:
    print("it was there!")
    print("condition")




sandwich_type = ""
subtotal = 0.0

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwich_type = input("Sandwich Choice: ")

# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

# Beverage Choice
bev_choice = input("Do you want a beverage? yes or no")
if bev_choice == "yes":
    bev_size = input("What size beverage would you like? Small, Medium, or Large")
    if bev_size == "small":
        print("You chose small, so $1.00")
        subtotal += 1
    if bev_size == "medium":
        print("You chose medium, so $1.75")
        subtotal += 1.75
    if bev_size == "large":
        print("You chose large, so $2.25")
        subtotal += 2.25

# Fries
fry_choice = input("Do you want french fries? Yes or No")
if fry_choice == "yes":
    fry_size = input("What size fries would you like? Small, Medium, or Large")
    if fry_size == "small":
        supersize = input("Do you want to supersize that for $2? Yes or no")
        if supersize == "yes":
            fry_size = "large"
            subtotal += 2
        else:
            print("You chose small fries for $1")
            subtotal += 1
    elif fry_size == "medium":
        print("You chose medium for $1.50")
        subtotal += 1.50
    else:
        print("You chose large fries for $2")
        subtotal += 2

# Kethcup
ketchup = float(input("HJow many ketup packets would you like? $0.25 each"))
if ketchup >= 0:
    subtotal += ketchup * .25

if bev_choice == "yes" and fry_choice == "yes":
    subtotal -= 1

print(sandwich_type)
if bev_choice == "yes":
    print(bev_size)
if fry_choice == "yes":
    print(fry_size)

print(subtotal)

