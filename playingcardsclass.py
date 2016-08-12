#CREATOR: Jessica Napolitano
#FUNCTION: Creates a playing card which has the accessor
#methods to return the rank and suit of the specific playing card

from graphics import*
from random import*

class PlayingCard:
    """Goal of this function is to get the rank of each card and if they input Ace or two to the entry box,
       it should be converted to the proper rank of that card..."""

    #creates the playing card class with rank and suit parameters
    def __init__(self,rank,suit):

        """sets the variables"""

        #the rank and suit instance variables are created
        self.rank = rank - 1
        self.suit = suit

    #get rank method is created
    def getRank(self):
        """returns the rank of the card."""
        
        return self.rank

    #get suit method is created
    def getSuit(self):
        """returns the suit of the card"""
        
        return self.suit

    #this allows us to create the deck of playing cards based on rank list and suit dictionary
    def __str__(self):
        rankList = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        suitList = {'s':'spade','c':'clubs','h':'hearts', 'd':'diamonds'}

        #returns the string message 'rank of suit'
        return rankList[self.getRank()] + ' of ' + suitList[self.getSuit()]

   

def test():
    c= PlayingCard(12,'d')
    print(c)

    
if __name__=="__main__":
    test()
    
    
