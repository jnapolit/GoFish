#CREATOR: Jessica Napolitano
#FUNCTION: This class sets up the main parts of the go Fish game as well as implements
#key parts of the game such as checkPair, isDeckEmpty, gettotal, initDeal, whoStarts, GoFishPlayer,
#GoFishComp, and DealerPlays (which uses GoFishComp).



from graphics import *

from random import *

from playingcardsclass import *

from deckclass import *



class GoFish:

    #the class constructor has all the player and dealer list and sets to them to empty

    def __init__(self,cHand=[],pHand=[],gridSlotsP=[],gridSlotsC=[],imageListP=[],imageListC=[],pairP=[],pairC=[],pairListP=[],pairListC=[],pairHandP=[],pairHandC=[],blankcards=[]):



        #playing deck instance variable created and shuffled using deck class method

        self.playingDeck = Deck()

        self.playingDeck.shuffled()





        #for singluar cards

        self.cHand = cHand # for actual playing cards (contains rank)

        self.pHand = pHand # for actual playing cards (contains rank)

        self.gridSlotsP = gridSlotsP #for hand slots(coordinates)

        self.gridSlotsC = gridSlotsC #for hand slots(coordinates)

        self.imageListP=imageListP #for images

        self.imageListC=imageListC #for images 



        #for pairs 

        self.pairP=pairP # for pair slots (coordinates)

        self.pairC=pairC #for pair slots (coordinates)

        self.pairListP=pairListP #for images 

        self.pairListC=pairListC #for images

        self.pairHandP=pairHandP #for actual playing card (contains rank)

        self.pairHandC=pairHandC #for actual playing card (contains rank)
        

        #so you can't see computer's cards
        self.blankcards=blankcards



        #creates slots for the cards of the player and the cards of the computer to be drawn into 

        for i in range(13):

            PointP=(100+i*40,550)

            PointC=(100+i*40,100)            

            self.gridSlotsP.append(PointP)

            self.gridSlotsC.append(PointC)

            

        #creates slots for the pairs of the player and the cards of the computer to be drawn into    

        for i in range(50):

            PointP=(100+i*20,430)

            PointC=100+i*20,230

            self.pairP.append(PointP)

            self.pairC.append(PointC)



#------------------------------------------------------------------------------------------------------------------------

    #checks a hand(which is passed) for a card(which is also passed). If the card is in this hand then it will return the

            #index of that card in the the hand. Otherwise it will return None 

    def checkPair(self,Card,hand):

        """checks a hand(which is passed) for a card(which is also passed). If the card is in this hand then it will return the

            index of that card in the the hand. Otherwise it will return None"""

        

        for card in range(len(hand)):

            

            print(Card.getRank())

            print(hand[card].getRank())

            

            if Card.getRank()==hand[card].getRank():

                

                return card

#-----------------------------------------------------------------------------------------------------------------------

    #checks to see if the deck is empty. If it is it will return true, otherwise it will return False

    def isDeckEmpty(self):

        """checks to see if the deck is empty. If it is it will return true, otherwise it will return False"""

        if self.playingDeck.cardsLeft()==0:

            return True

        

        else:

            return False

            

            

#-----------------------------------------------------------------------------------------------------------------------

    #finds the total of the hand which is passed        

    def gettotal(self,hand):

        """finds the total of the hand which is passed """
        

        return (len(hand)/2)
#-----------------------------------------------------------------------------------------------------------------------




    #the initial dealing of cards 

    def initDeal(self,gwin):
        """deals a card, checks to see if this card is already in the hand. If it is not then it just adds it to the players hand.

        if it is in the players hand then it will take both of those cards and redraw them in the pair slots."""
        
                 

        #FOR PLAYER

        for i in range(5):
            
            Card=self.playingDeck.dealCard()



            index= self.checkPair(Card,self.pHand)

            print(index)

            

            if index !=None:



                self.pairHandP.append(Card)

                self.pairHandP.append(self.pHand[index])

                self.pHand.pop(index)

    

            else:

                self.pHand.append(Card)

            

                    

        for i in range(len(self.pHand)):

            imP=Image(Point(self.gridSlotsP[i][0],self.gridSlotsP[i][1]),'playingcards/'+ self.pHand[i].getSuit()+ str(self.pHand[i].getRank()) +'.gif')

            self.imageListP.append(imP)

            imP.draw(gwin)



        for i in range(len(self.pairHandP)):

            imP=Image(Point(self.pairP[i][0],self.pairP[i][1]),'playingcards/'+ self.pairHandP[i].getSuit()+ str(self.pairHandP[i].getRank()) +'.gif')

            self.pairListP.append(imP)

            imP.draw(gwin)

        

               

    

   

      



        #FOR COMPUTER

        for i in range(5):

            Card=self.playingDeck.dealCard()



            index= self.checkPair(Card,self.cHand)

            print(index)

            

            if index !=None:



                self.pairHandC.append(Card)

                self.pairHandC.append(self.cHand[index])

                self.cHand.pop(index)

    

            else:

                self.cHand.append(Card)

            

                

        for i in range(len(self.cHand)):

            imP=Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]),'playingcards/'+ self.cHand[i].getSuit()+ str(self.cHand[i].getRank()) +'.gif')

            self.imageListC.append(imP)

            imP.draw(gwin)

            fake= Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]), 'playingcards/b1fv.gif')

            self.blankcards.append(fake)

            fake.draw(gwin)

            



        for i in range(len(self.pairHandC)):

            imP=Image(Point(self.pairC[i][0],self.pairC[i][1]),'playingcards/'+ self.pairHandC[i].getSuit()+ str(self.pairHandC[i].getRank()) +'.gif')

            self.pairListC.append(imP)

            imP.draw(gwin)

                

#---------------------------------------------------------------------------------------------------------------------------------------------------           

    



    #So this function decides who goes first. If return true then player... else the computer

    def whoStarts(self):

        """So this function decides who goes first. If return true then player... else the computer"""

        player=1

        computer=0

        starts= randrange(0,2)

        if starts == player:

            return True

        else:

            return False



#------------------------------------------------------------------------------------------------------------------------------------------------------"""       

    

    #draws a card and gives to player. Must first check to see if this card that is draw is already in the players hand though. 

    def GoFishPlayer(self,gwin):

        """draws a card and gives to player. Must first check to see if this card that is draw is already in the players hand though."""

        #declares the boolean gotMatch which determines if the player got a match after drawing from the deck
        #draws card from deck

        gotMatch = False

        Card=self.playingDeck.dealCard()



        #checks to see if this card is in the players hand already

        index= self.checkPair(Card,self.pHand)

        print(index)


              

        #if it is in the players hand

        if index !=None:

            #put both of these cards in the pairhands and also remove the card that was previously in the players hand

            self.pairHandP.append(Card)

            self.pairHandP.append(self.pHand[index])

            self.pHand.pop(index)

            gotMatch = True



        #if it was not in the players hand before then just append the card drawn to the players hand

        else:

            self.pHand.append(Card)



        #undraw all the cards in the players hand   

        for i in range(len(self.imageListP)):

            self.imageListP[i].undraw()



        #redraw the cards in the players hand and append those images to the imageListP   

        for i in range(len(self.pHand)):

            imP=Image(Point(self.gridSlotsP[i][0],self.gridSlotsP[i][1]),'playingcards/'+ self.pHand[i].getSuit()+ str(self.pHand[i].getRank()) +'.gif')

            self.imageListP.append(imP)

            imP.draw(gwin)



        #draw all the cards in the pairhand and append those images to the pairListP   

        for i in range(len(self.pairHandP)):

            imP=Image(Point(self.pairP[i][0],self.pairP[i][1]),'playingcards/'+ self.pairHandP[i].getSuit()+ str(self.pairHandP[i].getRank()) +'.gif')

            self.pairListP.append(imP)

            imP.draw(gwin)

        return gotMatch

#-----------------------------------------------------------------------------------------------------------------------------------------------------"""

    def GoFishComp(self,gwin):

        """draws a card and gives to computer. Must first check to see if this card that is draw is already in the computer's hand though."""

        #draws card from deck

        Card=self.playingDeck.dealCard()



        #checks to see if this card is in the computers hand already

        index= self.checkPair(Card,self.cHand)

        print(index)



        #if it is in the computer hand 

        if index !=None:

            #put both of these cards in the pairhands and also remove the card that was previously in the computers hand

            self.pairHandC.append(Card)

            self.pairHandC.append(self.cHand[index])

            self.cHand.pop(index)

            

        #if it was not in the computers hand before then just append the card drawn to the computers hand

        else:

            self.cHand.append(Card)


            



        #undraw all the cards in the computers hand      

        for i in range(len(self.imageListC)):

            self.imageListC[i].undraw()
            


        #undraws all the blanks

        for i in range(len(self.blankcards)):
            
            self.blankcards[i].undraw()
            
            


        #redraw the cards in the computers hand and append those images to the imageListC     

        for i in range(len(self.cHand)):

            imP=Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]),'playingcards/'+ self.cHand[i].getSuit()+ str(self.cHand[i].getRank()) +'.gif')

            self.imageListC.append(imP)

            imP.draw(gwin)

            fake = Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]), 'playingcards/b1fv.gif')

            self.blankcards.append(fake)

            fake.draw(gwin)
         

           

            

        #draw all the cards in the pairhand and append those images to the pairListC   

        for i in range(len(self.pairHandC)):

            imP=Image(Point(self.pairC[i][0],self.pairC[i][1]),'playingcards/'+ self.pairHandC[i].getSuit()+ str(self.pairHandC[i].getRank()) +'.gif')

            self.pairListC.append(imP)

            imP.draw(gwin)

  

                

                

#------------------------------------------------------------------------------------------------------------------------------------------------------"""       



    #pick card randomly, sees it player has this card. If they do then it takes those cards

    #   and draws them in front of the computer. It keeps doing this until does not have this card. Then it Go's fish. 



    def DealerPlays(self, gwin):

        """pick card randomly, sees it player has this card. If they do then it takes those cards

       and draws them in front of the computer. It keeps doing this until does not have this card. Then it Go's fish. """


        #initalize so that it gets into the while loop

        index=0
        turn=False



        #So that it keeps doing this until there is not a match

        while index!=None:



            #pick a card randomly from the computers hand to see if the player has that card

            Ask4card=choice(self.cHand)

            print(Ask4card.getRank(),'rank')



            #check to see if the player has that card

            index= self.checkPair(Ask4card,self.pHand)



            #if the player has that card

            if index !=None:



                #then add those cards to the pairHandC and remove them from the player's and computer's hands 

                self.pairHandC.append(Ask4card)

                self.pairHandC.append(self.pHand[index])

                self.pHand.pop(index)

                self.cHand.remove(Ask4card)

                print('got pair')

                

                #undraws hands and clears the image list for their hands
                

                        #for comp

                for i in range(len(self.imageListC)):

                    self.imageListC[i].undraw()

                #undraws all the blanks

                for i in range(len(self.blankcards)):
                    
                    self.blankcards[i].undraw()


            


                        #for player

                for i in range(len(self.imageListP)):

                    self.imageListP[i].undraw()



                    

                

                #redraws new hand without that card and appends all those images to now empty image list. Also redraws all the pairs. 



                    #for comp

                for i in range(len(self.cHand)):

                    imP=Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]),'playingcards/'+ self.cHand[i].getSuit()+ str(self.cHand[i].getRank()) +'.gif')

                    self.imageListC.append(imP)

                    imP.draw(gwin)

                    fake = Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]), 'playingcards/b1fv.gif')

                    self.blankcards.append(fake)

                    fake.draw(gwin)



                    

                for i in range(len(self.pairHandC)):

                    imP=Image(Point(self.pairC[i][0],self.pairC[i][1]),'playingcards/'+ self.pairHandC[i].getSuit()+ str(self.pairHandC[i].getRank()) +'.gif')

                    self.pairListC.append(imP)

                    imP.draw(gwin)



                    #player

                for i in range(len(self.pHand)):

                    imP=Image(Point(self.gridSlotsP[i][0],self.gridSlotsP[i][1]),'playingcards/'+ self.pHand[i].getSuit()+ str(self.pHand[i].getRank()) +'.gif')

                    self.imageListP.append(imP)

                    imP.draw(gwin)



                for i in range(len(self.pairHandP)):

                    imP=Image(Point(self.pairP[i][0],self.pairP[i][1]),'playingcards/'+ self.pairHandP[i].getSuit()+ str(self.pairHandP[i].getRank()) +'.gif')

                    self.pairListP.append(imP)

                    imP.draw(gwin)



                if len(self.pHand)==0 or len(self.cHand)==0:

                    indexPair  = None

                    print('here comp')

                    return -1

                    break



            #if the asked for card is not in the players hand

            else:

                self.GoFishComp(gwin)

                print('no got pair')


                
                #undraws hands and clears the image list for their hands
                

                        #for comp

                for i in range(len(self.imageListC)):

                    self.imageListC[i].undraw()

                #undraws all the blanks

                for i in range(len(self.blankcards)):
                    
                    self.blankcards[i].undraw()

              


                        #for player

                for i in range(len(self.imageListP)):

                    self.imageListP[i].undraw()

                

                    

                

                #redraws new hand without that card and appends all those images to now empty image list. Also redraws all the pairs. 



                    #for comp

                for i in range(len(self.cHand)):

                    imP=Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]),'playingcards/'+ self.cHand[i].getSuit()+ str(self.cHand[i].getRank()) +'.gif')

                    self.imageListC.append(imP)

                    imP.draw(gwin)

                    fake = Image(Point(self.gridSlotsC[i][0],self.gridSlotsC[i][1]), 'playingcards/b1fv.gif')

                    self.blankcards.append(fake)

                    fake.draw(gwin)



                    

                for i in range(len(self.pairHandC)):

                    imP=Image(Point(self.pairC[i][0],self.pairC[i][1]),'playingcards/'+ self.pairHandC[i].getSuit()+ str(self.pairHandC[i].getRank()) +'.gif')

                    self.pairListC.append(imP)

                    imP.draw(gwin)



                    #player

                for i in range(len(self.pHand)):

                    imP=Image(Point(self.gridSlotsP[i][0],self.gridSlotsP[i][1]),'playingcards/'+ self.pHand[i].getSuit()+ str(self.pHand[i].getRank()) +'.gif')

                    self.imageListP.append(imP)

                    imP.draw(gwin)



                for i in range(len(self.pairHandP)):

                    imP=Image(Point(self.pairP[i][0],self.pairP[i][1]),'playingcards/'+ self.pairHandP[i].getSuit()+ str(self.pairHandP[i].getRank()) +'.gif')

                    self.pairListP.append(imP)

                    imP.draw(gwin)
                

                if len(self.pHand)==0 or len(self.cHand)==0:

                    indexPair  = None

                    print('here comp')

                    return -1

                    break

        print('over')



       

       

        

#-------------------------------------------------------------------------------------------------------------------------------------------------------"""

       

     

def test():

    

   

    gwin=GraphWin("Black Jack", 900,660)



    pHand=[]

    cHand=[]

    gridSlotsP=[]

    gridSlotsC=[]

    imageListP=[]

    imageListC=[]

    pairP=[]

    pairC=[]

    pairListP=[]

    pairListC=[]

    pairHandP=[]

    pairHandC=[]

    

    myGoFish=GoFish(cHand,pHand,gridSlotsP,gridSlotsC,imageListP,imageListC,pairP,pairC,pairListP,pairListC,pairHandP,pairHandC)



    myGoFish.initDeal(gwin)

    

    #myGoFish.GoFishPlayer(gwin)

    

    myGoFish.DealerPlays(gwin)

    

    

    

    



if __name__ == "__main__":

    test()
