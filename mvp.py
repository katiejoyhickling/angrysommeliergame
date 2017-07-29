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
	print "However be careful, the Sommelier at the Haute Maison is crazy.\nIf you select a wine that doesn't pair with Chef Jacques food, he may mock you or ask you to leave, and that's not going to impress " + date_name +" is it?\n\n"

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
	wine_choice = raw_input("What is your selection?: ")
	wine_choice = int(wine_choice)
	if wine_choice == 0 :
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
	print "Your " + course_name + " today will be, " + course
	show_list(course_wine_list)
	wine_selection()

#------------PYTHON STARTS RUNNING FROM HERE------------

#Lists to be used in game play------

#meal wine lists

appetizer_wine_list = ["Moet & Chandon Champagne", "Vintage Merlot", "Australian Chardonnay", "Alsace Reisling" , "Trader Joe's 2 buck chuck"]
main_wine_list = ["Californian Sauvignon Blanc", "Old World Pinot Noir", "South African Chardonnay" , "Rhone Valley Shiraz"]
dessert_wine_list = ["Muscadelle", "Sauternes", "Pinot Gris", "Prosecco"]

#meal food lists

appetizers = ["Spinach and Goat upside down cake" , "Lobster-Avocado Cocktail" , "Salmon Rillettes with smoked kelp" , "Quadruple Baked Souffle with Port"]
mains = ["Skate wing with shaved sea ice" , "Pork cheeks in a black tuffle bao" , "Desconstructed Vegan Moussakka" , "Quail and dandelions with fermented pepper"]
desserts = ["A tea scented gateau with earl grey foam" , "Marscapone tower" , "A test tube of Black Forest Mousse" , "A edible balloon of pineapple smoked air"]

#End of lists-----------

#Playing is contained in a While Loop to allow game to be played again:

while True:

	#Welcome and set up statements:

	player_name = raw_input("What is your name? ")
	date_name = raw_input("What is your date's name?")
	welcome(player_name, date_name)

	#For extra fun and chaos a meal is selected at random from the lists and assigned to app, main and dessert variables used above
	# making it extra fun if you play the game again

	appetizer = random.choice(appetizers)
	main_course = random.choice(mains)
	dessert = random.choice(desserts)

	#Next section at your table welcome and meal variables:
	welcome_to_your_table = "Welcome to your table, I am your Sommelier, Ann Garry."

	#Play begins!

	#Appetizer
	print welcome_to_your_table
	course ("appetizer", appetizer, appetizer_wine_list)

	#Main Course
	course ("entree", main_course, main_wine_list)

	#Dessert
	course ("dessert", dessert, dessert_wine_list)

	#End of game

	play_again = raw_input("Thanks for playing, to play again enter Y: ").capitalize()
	if play_again != "Y":
		break







