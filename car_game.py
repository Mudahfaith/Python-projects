command = ""
started = False 

while True: 
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is alredy started")
        else:
            started = True
            print("Car Started")
    elif command == "stop":
        if not started: 
            print("Car is already stopped!")
        else:
            started = False 
            print("Car stopped.")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to quit the car")
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that!")