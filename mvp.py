#The Angry Sommelier!

"""

Winning conditions: Not Losing

Losing conditions: Picking the worst wine out of a selection of 4 in any of the 3 rounds

"""

#While loop for Game play


#Welcome and set up statements:

player_name = raw_input("What is your name? ")
date_name = raw_input("What is your date's name?")
welcome = "Welcome to the Haute Maison Restaurant," + player_name + "!" + "Thank you for bringing your date, " + date_name + " with you."
welcome_continued = "You have brought your date, "+ date_name + ", to the restaurant to impress them. Haute Maison is a very exclusive restaurant, you will be served a 3 course meal, selected by the Chef, Chef JacqueAss. You will be asked to select wines a la carte to go with your meal."
sommelier_intro = "However be careful, the Sommelier at the Haute Maison is crazy. If you select a wine that doesn't pair with Chef Jacques food, he may mock you or ask you to leave, and that's not going to impress " + date_name +" is it?"

#While loop, but just loops over print welcome and user choice, needs work
# playing = True
# while playing:
# 	print welcome
# 	user_choice = raw_input("Would you like to continue to your table (enter Y) or exit (enter E)?: ").capitalize()
# 	if user_choice == "E":
# 		playing = False


print welcome_continued
print sommelier_intro

# I need to work out this commented out section below, this doesn't make sense right now, this is optional really though:
#continue_choice = rawinput("If you wish to continue to your table and meet the sommelier, please follow me by typing 'follow'")
#	if "follow" then playing = true
#	else print "Sorry to lose you " + player_name + ", I hope you will return to this madhouse soon! Mwahaha!"

#meal wine lists

appetizer_wine_list = ["Moet & Chandon Champagne", "Vintage Merlot", " Australian Chardonnay", "Alsace Reisling" , "Trader Joe's 2 buck chuck"]
main_wine_list = ["Californian Sauvignon Blanc", "Old World Pinot Noir", "South African Chardonnay" , "Rhone Valley Shiraz"]
dessert_wine_list = ["Muscadelle", "Sauternes", "Pinot Gris", "Prosecco"]

#meal food lists

appetizers = ["Spinach and Goat Cheese Tartlet" , "Lobster-Avocado Cocktail" , "Salmon Rillettes" , "Twice Baked Souffle with Port Sauce"]
mains = ["Skate wing in cream sauce" , "Pork cutlets with a cranberry jus" , "Desconstructed vegan Moussakka"]
desserts = ["A tea scented gateau with earl grey foam" , "Marscapone tower" , "Black forest Mousse"]

#For extra fun and chaos a meal is selected at random from the lists and assigned to app, main and dessert variables used above
# making it extra fun if you play the game again

import random

appetizer = random.choice(appetizers)
main_course = random.choice(mains)
dessert = random.choice(desserts)

#Next section at your table welcome and meal variables:

welcome_to_your_table = "Welcome to your table, I am your Sommelier, Ann Garry."
your_appetizer = "Your appetizer today will be, " + appetizer
your_main_course = "Your main course today will be, " + main_course
your_dessert = "Your dessert today will be, " + dessert

#Show list Function

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
		print "Get out of my restaurant!" 
	elif wine_choice == 1 :
		print "Good Choice! You are a great catch"
	else:
		print "I guess that's OK, humph, your judgement is questionable..."

#Appetizer play begins!

print welcome_to_your_table
print your_appetizer
show_list(appetizer_wine_list)
wine_selection()


#Main Course
print your_main_course
show_list(main_wine_list)
wine_selection()

#Dessert
print your_dessert
show_list(dessert_wine_list)
wine_selection()


# #Need to change this into FUNCTIONS and WHILE LOOPS to ensure play continues or ends where it is logical to do so. 

# #Main Course play begins! Do I need a segue between Appetizer and main course??

# print your_main_course
# print select_a_wine
# print main_wine_list

# selection = raw_input("What is your selection?: ")
# #	if : (top wine selection, reward user)
# #	elif: (worst wine selection, kick user out of the restaurant!)
# #	else: (mediochre wine selection, user mocked)

# #Need to change this into FUNCTIONS and WHILE LOOPS to ensure play continues or ends where it is logical to do so. 

# #Dessert play begins! Do I need a segue between Main Course and Dessert? 

# print your_appetizer
# print select_a_wine
# print appetizer_wine_list

# selection = raw_input("What is your selection?: ")
# #	if : (top wine selection, reward user)
# #	elif: (worst wine selection, kick user out of the restaurant!)
# #	else: (mediochre wine selection, user mocked)

# #Need to change this into FUNCTIONS and WHILE LOOPS to ensure play continues or ends where it is logical to do so. 






