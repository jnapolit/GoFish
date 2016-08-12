*****************************************************************************************
Author : Jessica Napolitano 
Created: 4/29/2014

Modification Date         Name                      Description   
7/7/2015		  Jessica Napoltiano 	    Updated graphics with background
						    and a bug that if the player clicked 
						    anywhere except their cards it would take
						    it as a card the computer did not have and
					            make them goFish

*****************************************************************************************



WHAT TO RUN: 
	
	To play the game run the class called goFishmain.py. To test to make sure that the game was running accurate, the computer's cards started out as visible however, 
once testing was complete, the cards were flipped back over and made hidden so that the player could not cheat. 



DESCRIPTION :

    	For my final project, I made an interactive game of Go Fish. This is a card game where the player and the computer are competing to see who can get the largest
number of pairs before either player runs out of cards or before the deck is empty.They will take turns asking each other for a card. If their opponent does not have
the card they requested, they must draw a card from the deck. This is called 'Going Fish'. 



DESCRIPION OF MAJOR CLASSES AND METHODS: 

	So the first class I created was the playing card class. In this class, I made the getRank and getSuit methods which would be utalised later. What get
rank does is basically it gets the rank of the card. The rank is the value of the card (So 2 has a rank of 2, Ace has a rank of 1, and jack has a rank of 11. It goes up to 13). 
The getSuit method similarly returns the suit of the card (So either heart, diamond, spade, clover). 

	The next class I created was the deck class. In it, I initally made a deck of cards utalising the previous playingcard class and two for loops. I then made 3 helpful
methods that I will implement later on. The first method was was the shuffled method. This method does what it says, it shuffles the list of cards that I just created. The 
next method was called dealcard. This pops a card from the the deck and returns it as long as the deck is not empty. The final method just returns however many cards
are left in the deck. 

	The next class I created was called the buttonclass. This class consists of methods called: deactivate, activate, getlabel, and clicked. The activate and deactivate
do what they say. They allow the button to be clicked if it is active and if it is not activate, it changes the color to a more light gray and makes it so that the user
cannot click it. Getlabel simply returns the label of the button and clicked returns either True, you clicked it or False, you did not click it. 

	The final class I created prior to making the final main function was called goFishclass. So the first method I made in this class was checkPair. This method takes two arguments, one being a card and another
being a hand. The function of it is to take the card which was passed and see if it is in the hand which was also passed. If their is a card of this same rank in the hand
then it will return the index of that card that matches that rank which is in the hand. If there is not a card which has the same rank in the hand, then it will return NONE. 
The next method is called isdeckempty and it does what it says. It checks to see if the deck is empty. If it is then it returns true. If not then it returns false. The 
initdeal method deals the initial 5 cards to both the player and the computer. It also checks to see whethere any of these first cards are a pair and if they are they draw
them out in front of the person. The whostarts method randomly picks a number 0 or 1 and then based on this number, it determines who starts first. If it chooses 1 thne
the player starts and if it chooses 0 then it is the computer's turn first. The next two classes are goFish for the player and goFish for the computer. Both of them draw
a card from the deck and then add it to the player's hand. If there is a card already matching that rank and it makes a pair then it takes the card out of the players hand
and with the card that was drawn from the deck, they are then drawn in front of the player and or computer. The final method is called dealer plays. It picks a card randomly from the comp's hand,
sees it player has this card. If they do then it takes those cards and draws them in front of the computer. It keeps doing this until the player does not have this card. Then it Go's fish.

	All of these classed culminated inside the main function which in itself is completely commmented so that it is easier to follow... 


WAYS TO IMPROVE: 
	
	I also hope to make the computer play less random by keeping track of the cards they have previously asked for. In addition if the player just got a match of Jacks,
to not ask for Jacks and instead wait since the likelyhood that they have another Jack in their hand is very low. 

