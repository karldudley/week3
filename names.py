# declare variables to control loop
i = 0
enter_names = True

# loop until user enter stop
while enter_names:
    name = input("Enter Student Name (Stop to Exit):\t").lower()

    if name == "stop":
        enter_names = False
    else:
        i += 1
# print the number of students in the class
print(f"There are {i} students in the class.")
