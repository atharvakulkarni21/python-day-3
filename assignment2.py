# Prime numbers Assignment 2

num = int(input("enter the number "))
count = 0
i = 2
while(i <= num//2):
    if(num % i == 0):
        count = count + 1
        break
    if (count == 0 and num != 1):
        print(num, " is Prime Number")
else:
    print(num, " is Not a prime number")