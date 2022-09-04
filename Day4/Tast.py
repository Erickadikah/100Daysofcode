print("welcome to internal revenue services.")
gross = float(input("what is your gross income\n"))
if gross >= 1000:
    print("pay 5% tax")
    if gross >= 2000:
        print("pay tax 10%")
        if gross >= 5000:
            print("pay 15% tax")
        else:
            print("pay 17% tax")
