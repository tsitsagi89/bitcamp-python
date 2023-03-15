i=50
print("amount due " + str(i))
while True:
    coin=int(input("insert coin "))

    if coin== 5 or coin==10 or coin==25:
        i-=coin

        if i > 0:
            print("amount due " + str(i))

            continue
        elif i == 0:
            print("Change Owed " + str(i) )
            
            break
        elif i < 0:
            print("Change Owed " + str(i * -1)) 

            break   

                         
         

    
        