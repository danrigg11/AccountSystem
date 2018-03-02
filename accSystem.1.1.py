known_users = []

while True:
    print("Hi!My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("hello {}".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
            print("User {} removed".format(name))
            
        elif remove == "n":
            print("No problem {}, glad you stuck around".format(name))

    else:
        print("Hmmm i dont think i have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if add_me == "y":
            known_users.append(name)
            print("Welcome {}".format(name))
            
        elif add_me == "n":
            print("No problem {}, see you aorund.".format(name))
    

 
