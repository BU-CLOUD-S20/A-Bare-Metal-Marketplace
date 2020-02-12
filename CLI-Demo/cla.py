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
def add_credits():
  print("Please enter the ID of the Organization you would like to give credits to.")
  print("Here is a list of organizations you can give credits to.")
  print("Harvard ECE")
  print("MIT ECE")
  print("BU ECE")
  print("NEU ECE")
  while True:
    statement = input("> ")

    if statement == "Harvard ECE":
      credit_number = input("How many credits would you like to give to Harvard ECE? ")
      print("Transferred {} credits to Harvard ECE!".format(credit_number))
    elif statement == "MIT ECE":
      credit_number = input("How many credits would you like to give to MIT ECE? ")
      print("Transferred {} credits to MIT ECE!".format(credit_number))
    elif statement == "BU ECE":
      credit_number = input("How many credits would you like to give to BU ECE? ")
      print("Transferred {} credits to BU ECE!".format(credit_number))
    elif statement == "NEU ECE":
      credit_number = input("How many credits would you like to give to NEU ECE? ")
      print("Transferred {} credits to NEU ECE!".format(credit_number))
    elif statement == "quit":
      break
    else:
      print("Please enter a valid Organization ID or type quit to exit.")

def remove_credits():
  print("Please enter the ID of the Organization you would like to remove credits from.")
  print("Here is a list of organizations you can remove credits from.")
  print("Harvard ECE")
  print("MIT ECE")
  print("BU ECE")
  print("NEU ECE")
  while True:
    statement = input("> ")

    if statement == "Harvard ECE":
      credit_number = input("How many credits would you like to give to Harvard ECE? ")
      print("Transferred {} credits to Harvard ECE!".format(credit_number))
    elif statement == "MIT ECE":
      credit_number = input("How many credits would you like to give to MIT ECE? ")
      print("Transferred {} credits to MIT ECE!".format(credit_number))
    elif statement == "BU ECE":
      credit_number = input("How many credits would you like to give to BU ECE? ")
      print("Transferred {} credits to BU ECE!".format(credit_number))
    elif statement == "NEU ECE":
      credit_number = input("How many credits would you like to give to NEU ECE? ")
      print("Transferred {} credits to NEU ECE!".format(credit_number))
    elif statement == "quit":
      break
    else:
      print("Please enter a valid Organization ID or type quit to exit.")