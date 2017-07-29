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

# Wine Selection Function

def wine_selection():
	wine_choice = raw_input("\nWhat is your selection?: ")
	wine_choice = int(wine_choice)
	if wine_choice == 0:
		print "\nSommelier says: Get out of my restaurant!\n" 
		return False
	elif wine_choice == 1 :
		print "\nSommelier says: Good Choice! You are a great catch\n"
		return True
	else:
		print "\nSommelier says: I guess that's OK, humph, your judgement is questionable...\n"
		return True

#Course play function

def course (course_name, course, course_wine_list):
	print "\nYour " + course_name + " today will be, " + course + "\n"
	show_list(course_wine_list)
	good_selection = wine_selection()
	return good_selection

#Game function

#Notes on Game function:

#For extra fun and chaos a meal is selected at random from the lists and assigned to appetizer, main and dessert variables

#For all of the courses we are calling the course function. The course function calls the show list and wine selection functions, 
#wine selection not only prints the
#message to the user about their selection but returns a value, true or false,
#(this is assigned to a variable "good_selection" for ease of reading but doesn't need to be. 
#The value is used to break the while loop below.
#We use a conditional that if the return of the call of the function 'course' is False then the While loop breaks and play ends. 


def game():

	appetizer = random.choice(appetizers)
	main_course = random.choice(mains)
	dessert = random.choice(desserts)

	#Appetizer
	if course ("appetizer", appetizer, appetizer_wine_list) == False:
		return
	#Main Course
	if course ("entree", main_course, main_wine_list) == False:
		return
	#Dessert
	if course ("dessert", dessert, dessert_wine_list) == False:
		return

#------------PYTHON STARTS RUNNING FROM HERE------------

#Lists to be used in game play-----------------

#meal wine lists

appetizer_wine_list = ["Moet & Chandon Champagne", "Vintage Merlot", "Australian Chardonnay", "Alsace Reisling" , "Trader Joe's 2 buck chuck"]
main_wine_list = ["Californian Sauvignon Blanc", "Old World Pinot Noir", "South African Chardonnay" , "Rhone Valley Shiraz"]
dessert_wine_list = ["Muscadelle", "Sauternes", "Pinot Gris", "Prosecco"]

#meal food lists

appetizers = ["Spinach and goat cheese upside down cake" , "Lobster-Avocado Cocktail" , "Salmon Rillettes with salt-dried kelp" , "Quadruple Baked Souffle with Port Reduction"]
mains = ["Skate wing with shaved sea ice" , "Pork cheeks in a black tuffle bao" , "Desconstructed Vegan Moussakka" , "Quail and dandelions with fermented pepper"]
desserts = ["A tea scented gateau with earl grey foam" , "Marscapone tower" , "A test tube of Black Forest Mousse" , "An edible balloon of pineapple smoked air"]

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







