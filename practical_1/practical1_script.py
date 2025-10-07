#2.1
integer = -12
floating_point = 3.14
string = "Hello world!"
boolean = True
nonetype = None
list1 = [2,2,34,51,2,3]
dict1 = {"name": "Ellinor", "age": 22}
tuple1 = (10,20,30)
set1 = {1, 2, 3}
range1 = range(1,10)

print(boolean, type(boolean))

#2.2
if len(string) == 0:
    print("String is empty")

else:
    print("String is non-empty")
print("--------------------------------")

#2.2.1
if integer == 0:
    print("zero")
elif integer > 0:
    print("positive")
else:
    print("negative")
print("--------------------------------")

#2.2.2

#Solution were the type is hardcoded
x = [1,2,3]
if type(x) is list:
    print("Correct input type")
    if len(x) == 0:
        print("List is empty")
    elif len(x) == 1:
        print("List has a single item")
    else:
        print("List has multiple items")
else:
    print("Wrong input type")

#Solution without hardcodring the type and with user input (using directories "sequences")
sequences = {"list": list1, "tuple": tuple1, "range": range1}
choice = str(input("Choose one: list/tuple/range:"))

if choice in sequences:
    seq = sequences[choice]
    print("Correct input type")

    if len(seq) == 0:
        print("empty")
    elif len(seq) == 1:
        print("Single item")
    else:
        print("Multiple items")
else:
    print("Wrong input type")


