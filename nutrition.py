fruit = input("enter fruit: ")
item={
    "apple": 130,
    "avocado": 50,
    "Sweet Cherries": 100,
    "banana": 110,
    "lemon": 15 

}

if fruit == "apple":
    print("calories : " + str(item["apple"]))
elif fruit == "avocado":
    print("calories : " + str(item["avocado"]))
elif fruit == "Sweet Cherries":
    print("calories : " + str(item["Sweet Cherries"]))
elif fruit == "banana":
    print("calories : " + str(item["banana"]))
elif fruit == "lemon " :
    print("calories : " + str(item["lemon"]))
else:
    print("not list")              

    