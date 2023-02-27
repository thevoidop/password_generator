import random

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
num = "0123456789"
sym = '~!@#$%^&*()_+}{":?><|`-=]['']`}'

print("========== PASSWORD GENERATOR ==========\n\n")

inp = int(input("Enter the length of your password: "))

theqf = None
while (theqf != "q"):
    final = str()
    if inp < 8:
        print("Password length too short, try again. \n") 
    else:
        for i in range (inp):
            sel = random.randint(1,3)
            if sel == 1:
                add = random.choice(alp)
            elif sel == 2:
                add = random.choice(num)
            else:
                add = random.choice(sym)
            final = str(final) + str(add)
        print(f"\n{final}")
    theqf = input("\nEnter 'g' to generate again 'q' to quit: ")