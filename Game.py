import turtle # Activates the turtle graphics library to draw different places. 
import random # Imports the random library to randomly choose a function to execute.
import threading # Imports the threading library to run the timer in the background.
import time # Imports the time library to set the timer.

while True:
    #Configures the turtle graphics window. It is outside of the functions so that the rest of the program can interact with it.
    turtle.title("GuessDraw") # Sets the title of the window.
    t = turtle.Turtle() #Creates Turtle object that can be used for any function.
    t.hideturtle()# Hides the turtle cursor.
    t.speed(0) # Sets the speed of the turtle to the fastest.
    Point = [0,0,0,0] # A list to store the points of each player.
    # Functions to draw landmarks.
    def ben(): #Draws Big Ben
        global Show # Makes the variable global so that it can be used outside of the function.
        Show = "big ben"
        global Ans 
        Ans = Show.replace(" ", "") # Sets the answer to the question.
        global Country
        Country = "United Kingdom" # Sets the country of the landmark.
        
        t.penup()
        t.setposition(-100, -250)
        t.pendown()
        t.fillcolor("#e9a72c")
        t.pencolor("#e9a72c")

        #Creates base  of Big Ben. Height is 300 and width is 90
        t.begin_fill()
        t.goto(-10, -250)  
        t.goto(-10, 50)  
        t.goto(-100, 50)  
        t.goto(-100, -250) 
        t.end_fill()

        #creates head of Big Ben. Height is 100 and width is 120
        t.penup()
        t.goto(-115 , 50)
        t.pendown()
        t.fillcolor("#e9a72c")
        t.pencolor("#e9a72c")
        t.begin_fill()
        t.goto(-115,150)
        t.goto(5,150)
        t.goto(5,50)
        t.goto(-115 , 50)
        t.end_fill()
        

        #block on top of head. Height is 30 and width is 90
        t.penup()
        t.goto(-100,150)
        t.pendown()
        t.begin_fill()
        t.goto(-100,180) 
        t.goto(-10,180)
        t.goto(-10,150)
        t.end_fill()
        

        #create top part of Big Ben
        t.penup()
        t.goto(-100,180)
        t.pendown()
        t.pencolor("#272624")
        t.fillcolor("#03142E")
        t.begin_fill()
        t.goto(-10,180)
        t.goto(-25,235)
        t.goto(-85,235)
        t.goto(-100,180)
        t.end_fill()
        

        t.begin_fill()
        t.pencolor("#e9a72c")
        t.fillcolor("#e9a72c")
        t.penup() 
        t.goto(-25, 235)
        t.pendown()
        t.goto(-25 , 260)
        t.goto(-85, 260)
        t.goto(-85, 235)
        t.goto(-25, 235)
        t.end_fill()
        

        #create pointy part of Big Ben
        t.penup()
        t.goto(-25 , 260)
        t.pencolor("#272624")
        t.fillcolor("#03142E")
        t.pendown()
        t.begin_fill()
        t.goto(-55,330)
        t.goto(-85,260)
        t.end_fill()
        

        #create the clock face
        t.penup()
        t.pencolor("#000000")
        t.fillcolor("#e6cf00")
        t.goto(-95,140)
        t.pendown()
        t.begin_fill()
        t.goto(-15,140)
        t.goto(-15,60)
        t.goto(-95,60)
        t.goto(-95,140)
        t.end_fill()

        #Create the clock 
        t.penup()
        t.goto(-55,65) # start point of drawing the clock. 
        t.begin_fill()
        t.pendown()
        t.fillcolor("#FFFFFF") #white clock face
        t.pensize(5)
        t.setheading(0)  # Set the heading to 0 degrees (facing right)
        t.circle(35) #radius of clock face
        t.end_fill()

        # Create the clock hands
        t.penup()
        t.goto(-55,100) # Centre of clock face
        t.pendown()
        t.pensize(3) #thickness of clock hands
        t.goto(-55, 130) # hour hand
        t.penup()
        t.goto(-55,100)
        t.pendown()
        t.goto(-35, 95)  # minute hand
    def arc():  # Draws Arc de Triomphe
        global Show  # Makes the variable global so that it can be used outside of the function.
        Show = "arc de triomphe"
        global Ans 
        Ans = Show.replace(" ", "") # Value program uses to check answer. Spaces are removed in from inputs so that players don't have to worry about spaces when typing answers.
        global Country
        Country = "France"
        
        t.penup()
        t.setposition(-150,-250) #Sets the starting position of the turtle
        t.fillcolor("#f5ab79")
        t.pencolor("#f5ab79")
        t.begin_fill()
        t.pendown()
        #creating structure of arc de triomphe
        t.goto(-330,-250)
        t.goto(-330,200)
        t.goto(200,200)
        t.goto(200,-250)
        t.goto(20,-250)
        t.goto(20,50)
        t.goto(-150,50)
        t.goto(-150,-250)
        t.end_fill()
        #decorating the pillars of the arc de triomphe

        #creating marks each one is 200 pixels long
        #right mark
        t.penup()
        t.pencolor("#934632")
        t.goto(-340,-30)
        t.pensize(7)
        t.pendown()
        t.goto(-140,-30)

        #left mark
        t.penup()
        t.goto(10,-30)
        t.pendown()
        t.goto(210,-30)
        t.penup()

        #Rectangles
        #left rectangle (125 width and 35 height)
        t.fillcolor("#934632")
        t.begin_fill()
        t.goto(170,-5)
        t.pendown()
        t.goto(45,-5)
        t.goto(45,30)
        t.goto(170,30)
        t.goto(170,-5)
        t.end_fill()
        t.penup()

        #right rectangle (125 width and 35 height)
        t.begin_fill()
        t.goto(-300,-5)
        t.pendown()
        t.goto(-175,-5)
        t.goto(-175,30)
        t.goto(-300,30)
        t.goto(-300,-5)
        t.end_fill()
        t.penup()

        #Creating the top details
        #top rectangle (530 width and 10 height)
        t.begin_fill()
        t.goto(-330,70)
        t.pensize(1)
        t.pendown()
        t.goto(200,70)
        t.goto(200,110)
        t.goto(-330,110)
        t.goto(-330,70)
        t.end_fill()
        t.penup()

        #Creating the top line, 550 pixels long
        t.pensize(10) 
        t.goto(-340,120)
        t.pendown()
        t.goto(210,120)

        #Creating the arch 
        t.begin_fill()
        t.pensize(1)
        t.penup()
        t.goto(10, -30)
        t.pendown()
        t.setheading(90)  # Face upwards so semicircle drawn horizontally
        t.circle(75, 180)  #Draw semicircle
        t.goto(-150,-30)
        t.goto(-150,50)
        t.goto(20,50)
        t.goto(20,-30)
        t.goto(10,-30)  # Close the semicircle
        t.end_fill()
    def parth():#Draws the Parthenon
        global Show
        Show = "parthenon"
        global Ans # Makes the variable global so that it can be used outside of the function.
        Ans = Show.replace(" ", "") # Sets the answer to the question.
        global Country
        Country = "Greece" # Sets the country of the landmark.
        t.penup()
        t.setposition(-285,-250) #Sets the starting position of the turtle
        t.pendown()
        t.pencolor("#f5d7a3")
        t.fillcolor("#f5d7a3")
       
        #Creates base of the Parthenon. Height is 30 and width is 570
        t.begin_fill()
        t.goto(285,-250)
        t.goto(285,-220)
        t.goto(255,-220)
        t.goto(-285,-220)
        t.goto(-285,-250)
        t.end_fill()
        #Creates the 2nd block of base. Height is 20 and width is 540. 
        t.penup()
        t.goto(270,-220)
        t.pendown()
        t.begin_fill()
        t.goto(270,-200)
        t.goto(-270,-200)
        t.goto(-270,-220)
        t.end_fill()
        t.penup()
        #Creates the pillars of the Parthenon. Each pillar is 30 pixels wide and 250 pixels tall. 
        #Distance between each pillar is 42.8125 because the end of final pillar lines up with the end of its base. 
        for x in range(8): #draws 8 pillars
            t.begin_fill()
            t.goto(-270 + 72.8125 * x,-200)
            t.pendown()
            t.goto(-270 + 72.8125 * x ,50)
            t.goto(-240 + 72.8125 * x ,50)
            t.goto(-240 + 72.8125 * x ,-200) 
            t.end_fill()
            t.penup() 

        #Creates the top block of the Parthenon. Height is 75 and width is 520
        t.goto(270,50)
        t.pendown()
        t.begin_fill()
        t.goto(270,125)
        t.goto(-270,125)
        t.goto(-270,50)
        t.goto(270,50)
        t.end_fill()
        t.penup()

        #Creates the top triangle of the Parthenon.
        t.begin_fill()
        t.goto(300,125)
        t.pendown()
        t.goto(0,230)
        t.goto(-300,125)
        t.goto(300,125)
        t.end_fill()
        t.penup()

        #Create inner triangle of the Parthenon.
        t.begin_fill()
        t.fillcolor("#A39170")
        t.goto(240,135)
        t.pendown()
        t.goto(-240,135)
        t.goto(0,210)
        t.goto(240,135)
        t.end_fill()    
    def pal():#Draws Palazzo Vecchio
        global Show
        Show = "palazzo vecchio"
        global Ans # Makes the variable global so that it can be used outside of the function.
        Ans = Show.replace(" ", "") # Value program uses to check answer. Spaces are removed in from inputs so that players don't have to worry about spaces when typing answers.
        global Country
        Country = "Italy"
        #Creates the base of Palazzo Vecchio
        #Height: 250 Width: 500
        t.penup()
        t.begin_fill() 
        t.pensize(1)
        t.color("#000000","#E4B142")
        t.setpos(-250,-75)
        t.pendown()
        t.goto(-250,-250)
        t.goto(250,-250)
        t.goto(250,-75)
        t.pensize(3)
        t.pencolor("#B3A52F")
        t.goto(-250,-75)
        t.end_fill()

        #Another block Height: 50 Width: 500
        t.begin_fill()
        t.pensize(1)
        t.pencolor("#000000")
        t.goto(-250,100)
        t.pensize(3)
        t.pencolor("#B3A52F")
        t.goto(250,100)
        t.pensize(1)
        t.pencolor("#000000")
        t.goto(250,-75)
        t.end_fill()

        #Another block Height: 150 Width: 500
        t.penup()
        t.begin_fill()
        t.goto(-250,100)
        t.pendown()
        t.goto(-250,150)
        t.pensize(3)
        t.pencolor("#B3A52F")
        t.goto(250,150)
        t.pensize(1)
        t.pencolor("#000000")
        t.goto(250,100)
        t.pencolor("#B3A52F")
        t.goto(-250,100)
        t.end_fill()
        t.penup()

        turtle.tracer(0) # Disables animation for faster drawing.
        t.begin_fill()
        for i in range(20): # Creates the arches on the building.
            r = 12.5 # Radius of the semicircle.
            x = 250 - (i * 2*r) # Calculates the x-coordinate for each window.
            t.goto(x,150)
            t.pendown()
            t.pencolor("#000000")
            t.goto(x,200)
            t.setheading(90) # Resets the heading of the turtle to 90 degrees (facing up).
            t.circle(r,180) # Draws a semicircle
            t.goto(x - 2*r,150)
        turtle.tracer(1) # Re-enables animation.

        #Creates the block on top of arches. Width: 540 Height: 30
        t.goto(-270,197.5)
        t.goto(-270,227.5)
        t.pensize(3)
        t.pencolor("#B3A52F")
        t.goto(270,227.5)
        t.pensize(1)
        t.pencolor("#000000")
        t.goto(270,197.5)
        t.goto(250,150)
        t.end_fill() # Ends now to avoid colouring arches

        #Creates the block on top of the building. Width: 540 Height: 25
        t.penup()
        t.goto(-270,227.5)
        t.begin_fill()
        t.pendown()
        t.goto(-270,302.5)
        t.pencolor("#B3A52F")
        t.pensize(3)
        t.goto(270,302.5)
        t.pensize(1)
        t.pencolor("#000000")
        t.goto(270,227.5)
        t.end_fill()
        t.penup()
        t.goto(-270,302.5)
        t.pendown()
        t.begin_fill()
        t.goto(-270,327.5)
        for i in range(12): # Creates crenelations (square bits) on the castle. Height: 25 Width: 31.25
            x = t.xcor() # Records x-coordinate 
            t.goto(x,327.5)
            t.goto(x, 352.5)
            t.goto(x+31.25,352.5)
            t.goto(x+31.25,327.5)
            t.setheading(0) # Resets the heading of the turtle to 0 degrees (facing right).
            if i != 11: #Doesn't draw a gap on the final bit. 
                t.forward(15)
        t.goto(270,302.5)
        t.end_fill() # Ends fill for crenelations
    
    players = input("How many players? (1-4): ").replace(" ", "") # Asks the player how many players are playing the game. .replace() gets rid of spaces
    while players.isdigit() == False or int(players) < 0 or int(players) > 4: # Checks if input is a digit and within valid range
        if players.isdigit() == False:
            print("That isn't a number")
        elif int(players) < 1 or int(players) > 4:
            print("Please enter a number between 1 and 4")
        players = input("Please enter a valid number of players (1-4): ").replace(" ", "")
    players = int(players)
    if players < 1: #Game will pretend to be confused and then will end the program. A nice easter egg for players who try to break the game.
                print("Less than 1 person? \n" +
                      "Calculating... \n" * random.randint(3, 10) +
                      "Conclusion: \n" +
                      "At least one person needs to play the game. \n" +
                      "Without anyone playing, the game is pointless. \n" +
                      "Goodbye.")
                exit()
    if players == 1: # Informs the player about their difficulty options.
         print("Welcome to the GuessDraw! In this game, I will draw a landmark and you have to guess what it is. \n" \
        "You are playing solo so there are 3 difficulties: \n" \
        "Easy: You have unlimited time to guess and are told the country that you landmark is in. \n" \
        "Medium: You have unlimited time to guess. \n" \
        "Hard: You only have 30 seconds to guess. \n "\
        "Additionally, you can set a custom time limit" )
         D = input("First, choose your diifficulty (easy, medium, hard): ").lower().replace(" ", "")
         while D != "easy" and D != "medium" and D != "hard": # Ensures that the player enters a valid difficulty.
            D = input("First, choose your diifficulty (easy, medium, hard): ").lower().replace(" ", "")
         if D == "easy" or D == "medium": 
             ti = False
         if D == "hard":
             ti = 30
         Custom = input("If you want to set your own timer, how many seconds will it last? (type a bunch of letters if no): ").lower()
         if Custom.isdigit() == False and D == "hard":
             print("Timer set to 30 seconds, the default time for hard mode.")
         elif Custom.isdigit() == False:
             print("No timer set")
             ti = False
         else:
             ti = int(Custom)
             print(f"Timer set to {ti} seconds.")
    if players > 1: # modes for multiplayer are easy and medium. 
         ti = False # Sets time to false so that the game doesn't time the player.
         print("Welcome to the GuessDraw! In this game, I will draw a landmark and you have to guess what it is. \n" \
        "You are playing with a friend (or more) so there are 2 difficulties in multiplayer mode: \n" \
        "Easy: You have unlimited time to guess and are told the country that you landmark is in. \n " \
        "Medium: You have unlimited time to guess.")
         D = input("First, choose your difficulty (easy, medium): ").lower().replace(" ", "")  
         while D != "easy" and D != "medium": # Ensures that the player enters a valid difficulty.
            D = input("You need to choose your difficulty (easy, medium): ").lower().replace(" ", "")

    rounds = input("How many rounds do you want to play?: ").replace(" ", "")
    while rounds.isdigit() == False: # Checks if input is a digit to prevent game from crashing if it isn't. Player is stuck until they enter an integer.
        print("that isn't a valid number")
        rounds = input("Please enter a valid number of rounds: ")
    rounds = int(rounds) # Converts the input to a number.
    
    for i in range(rounds): # Starts the game loop. 
        functions = (ben, arc, parth, pal)  # List of functions to choose from.
        Draw = random.choice(functions)
        Draw()  # Execute the chosen function
        timeout = threading.Event() # Creates an event to signal the main thread that the timer is up.
        if ti != False: # If the timer is set, run the timer in the background.
            def timer(): #function to run timer in the background
                time.sleep(ti) # Waits for specified amount of time.
                timeout.set() # Send signal to notify that time is up. 
            t1 = threading.Thread(target=timer)
            t1.start() #Runs the timer in the background
        if D == "easy":
            print(f"This is from the country: {Country}") # Tells the player what country the landmark is in.
        Uans = input("What is the landmark? (if in multiplayer mode separate answers using a comma) ").lower()  
        if timeout.is_set() == True: # Goes to the next round since if time's up ,your answer is invalid.  
            print(f"The answer was: {Show}")
            print("Time is up!")
            continue
        else:
            t1 = None # Stops the timer thread if it was running.
        while Uans.count(",") != players - 1: # Makes sure all users' answers are accounted for. 
            Uans = input("Please re-enter your answer and separate multiple answers with commas: ").lower()  
        t.clear() 
    Uans = tuple(Uans.replace(" ","").split(",")) # Splits input into a tuple with no spaces in answers. A tuple uses less memory than a list so is better for this program.
    
    for x in range(players):# Loops through each player to check their answer and assign points.
            if Uans[x] == Ans:
                Point[x] += 1
                print(f"Player {x + 1} guessed correctly! You now have {Point[x]} points.")
            else:
                print(f"Player {x + 1} guessed incorrectly. The correct answer was {Show}. You still have {Point[x]} points.")
    
    print(f"Well done! You scored {Point[0]} out of {rounds} points!" if players == 1 else "")
    if Point.count(max(Point)) > 1 and players > 1: # If there is a tie, find the players with the maximum points and acknowledge their achievements
        maximum = [i + 1 for i, x in enumerate(Point) if x == max(Point)] # Find players with maximum points
        for i in range(len(maximum)- players): # Removes any extra players that may have been added to the list by accident so the announcement is correct. 
            maximum.pop()

        print(f"The winners are Players: {', '.join(map(str, maximum))} with {max(Point)} points!")  # If there is a tie, print all the winners. map convert each integer in the list to 
    else:
        print(f"You finished off with {Point[0]} points out of {rounds}!")  
                
    Replay = input("Would you like to play again? (Y or N) ").upper().replace(" ", "") # Asks the player if they want to play again. IF yes loop restarts, if no the program ends.
    if Replay == "Y" or Replay == "YES":
        print("Here we go again!")
        continue # Restarts the entire program so players can replay the game. 
    else:
        print("Goodbye!")
        turtle.bye() # Closes the turtle graphics window.
        exit()