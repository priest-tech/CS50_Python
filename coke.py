def coke():
    a=50
    total_payment=0

    print(f"amount due{a}")

    while total_payment < a:    
        b=int(input("Enter amount in multiples of 5: "))
        
        total_payment += b
        
        if  total_payment < a:
            print(f"amount due is: {a-total_payment}")
        elif total_payment > a:
            print(f"change due: {total_payment-a}, Enjoy you coke", sep="/n")
        else:
            print("Enjoy your coke")        

coke()     
