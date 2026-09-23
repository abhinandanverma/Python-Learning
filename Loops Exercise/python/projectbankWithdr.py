bal=10000
withdrawal = True
while withdrawal:
    amount = int(input("Enter amount withdrawal :"))
    if amount <=bal:
        print("amount debited")
        bal = bal-amount
        print("your corrent amount",bal)
    else:
        print("insvfficient bal")
    choice = input("do need to withdeawal again:")        
    if choice.lower()=="yes":
        withdrawal=True