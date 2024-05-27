a=int(input("Please Enter your age:\n "))
b=input(" Are you student? (yes or no)\n").lower()

if b == "yes":
    if (a <= 12) or (a<=18 and a>=13):
        print("You will get discount for your movie ticket")
    else:
        print("sorry la! your age exceed the discount citeria..so we couldn't help you with the discount la")

else:
    print("You have to buy movie ticket without discount la ")

