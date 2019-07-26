print("Hello World")
print("Bye World\r\n")

num1 = int(raw_input("Enter number #1: "))
num2 = int(raw_input("Enter number #2: "))
total = num1 + num2
print("The sum is\r\n " + str(total))


num = int(raw_input("Enter a number: "))
if num > 0:
    print("Thats not the diffrence! ")
    print("try again \r\n")
elif num < 0:
    print("Thats a Negative Number!")
else:
    print("Zero is neither positive nor negatvive\r\n")


string = "hello there\r\n"
for letter in string:
    print(letter.upper())

for i in range(5):
    print(i)

my_name = "Bob"
friend1 = "Alice"
friend2 = "John"
friend3 = "Mallory"

print(
 "My name is %s and my frineds are %s, %s, and %s\r\n2" %
 (my_name, friend1, friend2, friend3)
)


def greetAgent(first_name, last_name ):
    print("%s. %s %s. " % (last_name, first_name, last_name))
greetAgent("Bond", "James Bond "):
