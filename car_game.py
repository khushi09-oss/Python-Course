command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
        Start - to start the car
        stop - to stop the car
        quit - to quit the program""")
    elif command == "quit":
        break
    else:
        print("SORRY I DONT UNDERSTAND")



