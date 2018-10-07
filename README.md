[[BOMBERMAN GAME]]

Controls : 

	Quit game 	: q
	Move up		: w
	Move left	: a
	Move right	: d
	Move down	: s
	Drop bomb 	: b

Specifications Of The Game:
	
	# Game consists of the Bomberman and Enemies. 
	# Bomberman has 3 lives to play.
	# Bomberman has to kill all the enemies on a level to complete a given level.
	# Enemies can be killed if they are caught up in an explosion.
	# Only one bomb can be placed at a given time.
	# Bomberman gets a score of +100 on killing an enemy and a score of +20 on breaking a brick by a bomb.
	# The game is terminated if the bomberman loses his three lives or the user presses the key 'q' or he has completed 4 levels of the game.
	# At any time multiple enemies can share the same position and the bomberman can also share position with any enemy.

Additional Specifications:

	Symbols for the game :
		Walls 			: X
		Bricks 			: /
		Bomberman 		: B
		Enemy 			: E
		explosion 		: e
	    	bomb            	: counter(2,1,0)

Features implemented :
	# INHERITENCE : There is good use of inheritence. Enemy as well as the bomberman inherit their movement functions from the person class. There are instances of various functions being inherited from the board class in different classes.

	# Modularity : The entire game has been build in a modular fashion. Most of the jobs have their own dedicated functions which make the code modular and easy to understand.

	# Encapsulation : Encapsulation has been used to present many methods in various classes which are integral to the functioning of the game. Encapsulated variables are used in various function like printing the board, various movements and various bomb operations.

	# POLYMORPHISM : The use of polymorphism has been done to modify the 2D array which helps in movement of the enemy.

	# Bonus Implemented : 
		- Bomb displays the number of seconds left for the explosion (Timer is shown).
		- Implementation of extra levels (i.e till 4 in different levels there are different number of temproary bricks and enemy).
		- Different objects have different coloured symbols.
