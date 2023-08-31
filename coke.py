def coke():
    a=50
    total_payment=0

    print(f"amount due {a}")

    while total_payment < a:    
        b=int(input("Insert Coin: "))
        
        total_payment += b
        
        if  total_payment < a:
            print(f"Amount Due: {a-total_payment}")
        elif total_payment > a:
            print(f"Change Owned: {total_payment-a}, Enjoy you coke", sep="/n")
        else:
            print("Enjoy your coke")        

coke()     
