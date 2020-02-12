def main():
    print ("Welcome to Bare Metal Marketplace!")

    while True:
        statement = input("> ")
        print (statement)
        
        if statement == "get-user" :
          print("user?")
          statement = input("> ")
          print(statement)
          print("This is user!")


        if statement == "list-users" :
          print("List of users")

        if statement == "quit":
            break


        else :
          print("here is a list of commands")

if __name__ == "__main__":
    main()