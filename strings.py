name= input("who?").lower()

match name:
    case "obi-wan":
        print("\"These aren\'t the droids you\'re looking for.\"")


#BONUS

  

author_input = input("Who? ").lower()

author = {
    "mahatma gandhi": "\"Be the change that you wish to see in the world.\"",
    "friedrich nietzsche": "\"Without music, life would be a mistake.\"",
    "benjamin franklin" : "\"Go to heaven for the climate and hell for the company.\""
}

if author_input == "mahatma gandhi":
    print(author["mahatma gandhi"])
elif author_input == "friedrich nietzsche":
    print(author["friedrich nietzsche"])
elif author_input == "benjamin franklin":
    print(author["benjamin franklin"])
else:
    print("Author not found.")