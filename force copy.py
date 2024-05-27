print("Problem solving related to NEWTON SECOOND LAW") 
print("...................................................")

print("select the missing value:")
print("1. Mass(m)")
print("2. Acceleration(a)")
print("3. Force(f)")

missing_Value= input("Enter your missing option number: ")

if missing_Value == "1":
    f=float(input("Enter force(f): "))
    a=float (input("Enter acceleration(a): "))
    m=f/a
    print(f"mass= {m}")

elif missing_Value=="2":
    f=float(input("Enter force(f):" ))
    m=float(input("Enter mass(m):" ))
    a=f/m
    print(F"Acceleration= {a}")

elif missing_Value=="3":
    m=float(input("Enter mass(m): "))
    a=float(input("Enter acceleration(a): "))
    f=m*a
    print(f"Force= {f}")

else:
    print("invalid! plz enter the correct option")