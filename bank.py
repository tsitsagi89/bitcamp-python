bank=input("Greeting: ").lower()

match bank:
    case "hello":
        print("$0")
    case "h":
        print("$20")   
    case _:
        print("$100") 
