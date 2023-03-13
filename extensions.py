file_name = input("file extensions: ").lower()

name = file_name.split(".")
 
match name[1] :
    case "gif":
        print("image/gif"   )
    case "jpg":
        print("image/jpg") 
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")      
    case "zip":
        print("application/zip")      
    case _:
        print("application/octet-stream")