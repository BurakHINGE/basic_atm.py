a = 0

while True:    

    b = int(input("Please select a transaction\n\n1-Check Balance\n2-Deposit\n3-Withdraw\n4-Exit\n"))

    if b == 1:
        print(f"Your current balance: {a}")

    elif b == 2:
        c = int(input("Enter the amount you want to deposit: "))
        a = a + c 
        print(f"Your current balance: {a}")

    elif b == 3:
        d = int(input("Enter the amount you want to withdraw: "))

        if d <= a:
            a = a - d
            print(f"Your current balance: {a}")
        else:
            print("Insufficient funds in your account.")

    elif b == 4:
        print("Goodbye...")
        break
