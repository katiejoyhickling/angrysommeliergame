#The Angry Sommelier!

"""

Winning conditions: Not Losing

Losing conditions: Picking the worst wine out of a selection in any of the 3 rounds, which stops play

"""

#Importing Modules for use in game

import random 

#FUNCTIONS

#Welcome Function

def welcome (player_name, date_name):
	print "Welcome to the Haute Maison Restaurant, " + player_name + "! \n"+ "Thank you for bringing your date, " + date_name + " with you.\n"
	print "You have brought your date, "+ date_name + ", to the restaurant to impress them.\nYou will be served a 3 course meal, selected by Chef JacqueAss. \nYou will select wines to go with your meal.\n"
	print "However be careful, the Sommelier at the Haute Maison is crazy.\nIf you select a wine that doesn't pair with Chef Jacques food, he may mock you or ask you to leave, and that's not going to impress " + date_name +" is it?\n"
	continue_to_table = raw_input("\nWould you like to continue to your table or exit? Type Y to continue: ").capitalize()
	if continue_to_table == "Y":
		print "\nWelcome to your table, I am your Sommelier, Ann Garry."
		return True
	else:
		return False

#Show list function

def show_list (wine_list):

	print "Please select a wine from the wine list by number. The wine list is: "

	for index, wine in enumerate(wine_list):
		print "{}. {}".format(index,wine)

#Could also do like this: Tested, both work- 

	#for index in range(len(wine_list)):
    		#print "{}. {}".format(index,wine_list[index])

# Wine Selection Function, takes good and bad wines (tuple for each dish (values) paired with our dishes (keys) in our course dictionaries), decodes good and bad
#wines, takes input from user and then uses conditional to recognise good, bad wines and 'else' (other selections- medium choices)

def wine_selection(good_and_bad_wines):
	good_wine, bad_wine = good_and_bad_wines
	wine_choice = raw_input("\nWhat is your selection?: ")
	wine_choice = int(wine_choice)
	if wine_choice == bad_wine:
		print "\nSommelier says: Get out of my restaurant!\n" 
		return False
	elif wine_choice == good_wine:
		print "\nSommelier says: Good Choice! You are a great catch\n"
		return True
	else:
		print "\nSommelier says: I guess that's OK, humph, your judgement is questionable...\n"
		return True

#Course play function- takes the data about the course, calls show list and wine selection, and returns Boolean indicating if wine selection is good or not (True/False)

def course (course_name, course, course_wine_list, good_and_bad_wines):
	print "\nYour " + course_name + " today will be, " + course + "\n"
	show_list(course_wine_list)
	return wine_selection(good_and_bad_wines)
	

#Game function

#Notes on Game function:

#For extra fun and chaos a meal is selected at random from the dictionaries and assigned to appetizer, main and dessert variables, the random.choice(list (A))
#code here iterates over the dictionaries and makes a list of the keys, then selects from that list at random 

#For all of the courses we are calling the course function. The course function calls the show list and wine selection functions, 
#wine selection not only prints the
#message to the user about their selection but returns a value, true or false,
#(this is assigned to a variable "good_selection" for ease of reading but doesn't need to be. 
#The value is used to break the while loop below.
#We use a conditional that if the return of the call of the function 'course' is False then the While loop breaks and play ends. 


def game():

	appetizer = random.choice(list (appetizers))
	main_course = random.choice(list (mains))
	dessert = random.choice(list (desserts))

	#Appetizer
	if course ("appetizer", appetizer, appetizer_wine_list, appetizers[appetizer])== False:
		return
	#Main Course
	if course ("entree", main_course, main_wine_list, mains[main_course]) == False:
		return
	#Dessert
	if course ("dessert", dessert, dessert_wine_list, desserts[dessert]) == False:
		return

#------------PYTHON STARTS RUNNING FROM HERE------------

#Lists to be used in game play-----------------

#meal wine lists

appetizer_wine_list = ["Moet & Chandon Champagne", "Vintage Merlot", "Australian Chardonnay", "Alsace Reisling", "Trader Joe's 2 buck chuck"]
main_wine_list = ["Californian Sauvignon Blanc", "Old World Pinot Noir", "South African Chardonnay" , "Rhone Valley Shiraz"]
dessert_wine_list = ["Muscadelle", "Sauternes", "Pinot Gris", "Prosecco"]

#meal food lists

appetizers = {"Spinach and goat cheese upside down cake": (2 , 4), 
			  "Lobster-Avocado Cocktail": (0 , 2), 
			  "Salmon Rillettes with salt-dried kelp": (3 , 4), 
			  "Quadruple Baked Souffle with Port Reduction": (1 , 0)}

mains = {"Skate wing with shaved sea ice": (0 , 1), 
		 "Pork cheeks in a black tuffle bao" : (1 , 3), 
		 "Desconstructed Vegan Moussakka": (3 , 0), 
		 "Quail and dandelions with fermented pepper": (1 , 2)}

desserts = {"A tea scented gateau with earl grey foam": (0 , 3), 
			"Marscapone tower": (1 , 3) , 
			"A test tube of Black Forest Mousse": (3 , 1), 
			"An edible balloon of pineapple smoked air": (2 , 0)}

#End of lists-----------------------------------

#Playing is contained in a While Loop to allow game to be played again:

while True:

	#Welcome and set up statements:

	player_name = raw_input("What is your name? ")
	date_name = raw_input("What is your date's name?")
	if welcome(player_name, date_name) == False:
		break

	#Play begins! Calling the game function
	
	game()

	#End of game

	play_again = raw_input("THE END\nThanks for playing, to play again enter Y: ").capitalize()
	if play_again != "Y":
		break







