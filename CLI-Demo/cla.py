

def get_node():
    print("")
    print ("Welcome to the Node Dashboard!")
    print("You can enter the name of any node to receieve more information!")
    print("Here is a list of your nodes:")
    print("Node A, Status: In Use")
    print("Node B, Status: In Use")
    print("Node C, Status: In Use")
    print("Node D, Status: In Use")
    print("Node E, Status: In Use")
    while True:
        statement = input("> ")
        print (statement)
        
        if statement == "A" :
          print("Node: A ")
          print("Owner: You")
          print("Status: In Use")

        elif statement == "B" :
          print("Node: B")
          print("Owner: You")
          print("Status: In Use")

        elif statement == "C" :
          print("Node: C ")
          print("Owner: You")
          print("Status: In Use")

        elif statement == "D" :
          print("Node: D ")
          print("Owner: Harvard ECE")
          print("Status: Rented by You and In Use")
          print("Price: Bought at 11$ / hour")
          print("Time: 2.25 hours remaining")
          
        elif statement == "E" :
          print("Node: F ")
          print("Owner: MIT ECE")
          print("Status: Rented by You and In Use")
          print("Price: Bought at 10$ / hour")
          print("Time: 5.25 hours remaining")

        elif statement == "quit":
            break


        else :
          print("Please enter a valid node or type 'quit' to exit.")

