<h2><u> Libraries </u></h2>
<p> <b>No additonal installation required, make sure you are on the latest version of python and then you can run the code and play.</b></p>
<p> turtle - Draws landmark </p>
<p> random - Selects landmark to draw </p>
<p> threading - Used to run a timer in the backgorund </p>
<p> time - Runs a timer </p> 

<h2><u> How it works </u></h2>   
<p>First, turtle is set up and hidden.</p>
<p>The list "Points" stores all each players' points.Add one to the index number to figure out which player it corresponds to.  E.g index 0 for player 1. </p>
<p> .replace() is used to remove spaces from inputs and .lower() turn the input into lowercase so that inputs are processed equally and the desired outcome happens. 
<p> I have used while loops to trap the player until they give a valid input to prevent the game from crashing </p>
<p> Different difficulties are avilaible based on how many players. </p>
<p>Difficulties: </p>
<p> Easy - tells player the country with unlimited time,  availiable in single and multiplayer mode.</p>
<p> Medium - Provides unlimited time, availible in single and multiplayer mode.</p>
<p> Hard - Only 30 secs to answer, exclusive to single player mode </p>

<h2><u> The Game </u> </h2>
<p> After the user decides how many rounds they want to do, the for loop starts </p> 
<p> First, a landmark is chosen and drawn from the list. The function drawing fills in details needed by the program for marking. </p>
<p>Then, the timer starts if enabled and a hint is given if the user ask for it. </p>
<p>After recieving the input, the game checks if the timer has finished. If it has, then the input is wrong. </p>
<p>The game will check the commas in the input to make sure each player has their answer accounted for otherwise, they will need to retype their answer.</p>
<p>The game loops through each answer, and checking if they are correct rewarding the players with points. </p>
<p>After all the rounds are completed the game will replay or end based on the user's wants.</p>



