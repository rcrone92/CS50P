def main():
    file = input("File name: ")
    #print(file.split(".")[-1])
    match file.lower().strip().split(".")[-1]:
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "gif" | "png":
            print("image/" + file.lower().strip().split(".")[-1])
        case "pdf" | "zip":
            print("application/" + file.lower().strip().split(".")[-1])
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

if __name__ == "__main__":
    main()
