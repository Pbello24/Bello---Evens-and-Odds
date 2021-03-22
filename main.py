odd_count=0
even_count=0
n = 0



num = int(input("How many numbers do you want to check? "))


for x in range(num):
  n = int(input("Enter a number: "))
if (n % 2):
  print("{x} is an even number")
elif (n % 3):
  print("{x} is and odd number")
