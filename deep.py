text=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")


match text:
    case "42"| "Forty Two"| "forty-two":
        print("yes")
    case "50":
        print("no")    
    case _:
        print("no")    