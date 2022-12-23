# declare variables
num1 = int(input("Please enter a number:\t"))
i = 1

# Loop from 1 to chosen number. Print out the even number and iterate the loop
while i <= num1:
    if i % 2 == 0:
        print(i)
    i += 1
