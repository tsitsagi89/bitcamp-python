def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    for i in s[2:-2]:
        i.isdigit()
        return False



    if len(s) < 2 or len(s) > 6 :
        return False
    
    if s[0].isdigit() or s[1].isdigit():
        return False
    
    if s.isalnum():
        return True
    
    return True

main()