#CREATOR: Jessica Napolitano
#FUNCTION: This program drives the whole application by using the other classes. It has one function
#called mainmenu which is used to set up the mainmenu which has the options to either
#play the game, view the rules, or look over some strategy. The main function then
#creates an instance of GoFish and uses the other classes and logic to create the application.


from random import *

from playingcardsclass import *

from deckclass import *

from goFishclass import*

from buttonclass import*

from time import*



def mainmenu(gwin):

            background = Image(Point(500,320),'Img11297_large.gif')
            
            background.draw(gwin)
                    

            greeting = Text(Point(500,330),"GO FISH")

            greeting.setSize(32)

            greeting.setFill('white')

            greeting.setStyle('bold')

            greeting.draw(gwin)


            rulesButton=Button(gwin,Point(300,550),100,100,'RULES')

            rulesButton.activate()

            rulesButton.setFill(color_rgb(60,179,113))

            strategyButton= Button(gwin,Point(500,550),100,100,'STRATEGY')

            strategyButton.activate()

            strategyButton.setFill(color_rgb(32,178,170))

            playButton = Button(gwin,Point(700,550),100,100,'PLAY')

            playButton.activate()

            playButton.setFill(color_rgb(60,179,113))

            return rulesButton, strategyButton, playButton

def main():    

    #makes window

    gwin=GraphWin('GO Fish',1000,660)

    
    #menu page
   
    
    rulesButton, strategyButton, playButton = mainmenu(gwin)      

  
    pt = gwin.getMouse()


    while playButton.clicked(pt) == False:
        

        if rulesButton.clicked(pt)==True:
            
            gwin.delete("all")

            
            background = Rectangle(Point(0, 0), Point(1000, 660))
            
            background.setFill(color_rgb(30,144,255))
            
            background.draw(gwin)


            sticker = Image(Point(500,120),'fishsticker.gif')
            
            sticker.draw(gwin)
            
            
            backbutton = Button(gwin,Point(900,100),100,100, 'BACK')
            
            backbutton.activate()
            
            backbutton.setFill(color_rgb(60,179,113))
            

            instructions = Text(Point(500,430),"""RULES OF GO FISH

        GOAL: Obtain as many pairs of cards as you can. A pair is two cards with the

          same rank.           

        HOW GAME WILL RUN: A player (either the computer or you) will be chosen randomly

          to go first. Upon your turn, you will be able to enter a number ranging from
          
          1 to jack, queen, king, and ace and ask the computer if they have that specific
          
          rank card. If the computer has that card, your pair will then be displayed face
          
          up in front of you. If the computer has the card you request you may then go again.
          
          It stays your turn until the computer does not have the rank you ask for. You  then
          
          must "GO Fish" which means you will be dealt a card. It then switches to the
          
          computer's turn. The computer will ask you for a certain card, and if it is in
          
          your hand the program will automatically take it from you and place it face up
          
          in front of the computer with their matching card. This will continue on until
          
          either the deck has run out or until a player runs out of cards in their hand.
          
          The total number of pairs will then be totaled and whoever has the most will win!""")

            instructions.setFill(color_rgb(	46,139,87))

            instructions.setSize(9)

            instructions.setStyle('bold')

            instructions.draw(gwin)

            pt = gwin.getMouse()

            #while the user is not clicking the back button

            while backbutton.clicked(pt)!=True:

                pt = gwin.getMouse()

            mainmenu(gwin)
                

        elif strategyButton.clicked(pt)==True:
            
            gwin.delete("all")

           
            
            background = Rectangle(Point(0, 0), Point(1000, 660))
            
            background.setFill(color_rgb(30,144,255))
            
            background.draw(gwin)


            sticker = Image(Point(500,120),'fishsticker.gif')
            
            sticker.draw(gwin)

             
            backbutton = Button(gwin,Point(900,100),100,100, 'BACK')
            
            backbutton.activate()
            
            backbutton.setFill(color_rgb(60,179,113))



            instructions = Text(Point(500,430),"""STRATEGY OF GO FISH

        Try to rememeber what cards you have already asked the computer for. If it has

          not drawn a card between now and then, then it still won't have that card. Also look

          at what matches the computer just laid down. The odds that the computer had 3 of a kind

          is unlikely. So you should wait a few turns and let the computer draw from the deck

          before you ask for that card""")

            instructions.setFill(color_rgb(46,139,87))

            instructions.setSize(9)

            instructions.setStyle('bold')

            instructions.draw(gwin)

            #while the user is not clicking the back button

            while backbutton.clicked(pt)!=True:

                pt = gwin.getMouse()

            mainmenu(gwin)
            
            
        pt = gwin.getMouse()


    
    #otherwise playButton has been clicked        


    #set up background

    gwin.delete('all')

    background = Image(Point(500,120),'fishbackground.gif')
            
    background.draw(gwin)


   #initalizing variables
    
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

    blankcards=[]

    
    #makes new game
    
    game= GoFish(cHand,pHand,gridSlotsP,gridSlotsC,imageListP,imageListC,pairP,pairC,pairListP,pairListC,pairHandP,pairHandC,blankcards)

    


    

    #buttons: exit, newgame,keys for the player to pick what card they want to ask for    

    exitButton=Button(gwin,Point(880,550),30,30,'Exit')

    exitButton.activate()

    exitButton.setFill(color_rgb(60,179,113))

    

    newgameButton=Button(gwin, Point(940,550),80,30,'New Game')

    newgameButton.activate()

    newgameButton.setFill(color_rgb(60,179,113))


    #only need to make 13 spots since if have more than 13 cards then one of them must be a match. So
    #make 13 buttons and put them all into a list

    keys=[]

    for i in range(13):

        key = Button(gwin, Point(gridSlotsP[i][0]-10,gridSlotsP[i][1]),40,100, "")

        key.deactivate()

        key.setFill(color_rgb(60,179,113))

        keys.append(key)




    #making a picture of a deck

    Deck= Image(Point(900,300),'playingcards/b1fv.gif')

    Deck.draw(gwin)

    


    #initalizing game with first deal, messages, choosing who goes first. 

    game.initDeal(gwin)

    

    totalP= game.gettotal(pairHandP)

    TotalP1=Text(Point(900,360),"Player's Total:")

    TotalP1.draw(gwin)

    TotalP2=Text(Point(970,360),'0')

    TotalP2.setText(totalP)



    totalC= game.gettotal(pairHandC)

    TotalC1=Text(Point(900,240),"Computer's Total:")

    TotalC1.draw(gwin)

    TotalC2=Text(Point(980,240),'0')

    TotalC2.setText(totalC)


    
    turn=game.whoStarts() #player= true///comp = false

        

    if turn==True:   

        message=Text(Point(450,330),"""It's YOUR TURN! CLICK to start then, click on the card you wish

                     to ask the Comp for""")

        message.draw(gwin)

        

    elif turn==False:

        message=Text(Point(450,330),"It's the COMPUTER'S TURN first! CLICK to start")

        message.draw(gwin)

      

    

    #click to get game started

    pt=gwin.getMouse() 



    totalP = 0

    totalC = 0

    #while you have not clicked the exit button

    while exitButton.clicked(pt)==False:

        #if you click new game then clear everything from the window and redraw/ reinitalize everything and make a new instance of the game

        if newgameButton.clicked(pt)==True:
            
            gwin.delete('all')

            background = Image(Point(500,120),'fishbackground.gif')
            
            background.draw(gwin)

            exitButton=Button(gwin,Point(880,550),30,30,'Exit')

            exitButton.activate()

            exitButton.setFill(color_rgb(60,179,113))
            

            newgameButton=Button(gwin, Point(940,550),80,30,'New Game')

            newgameButton.activate()

            newgameButton.setFill(color_rgb(60,179,113))
            

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

            blankcards=[]

            

            game= GoFish(cHand,pHand,gridSlotsP,gridSlotsC,imageListP,imageListC,pairP,pairC,pairListP,pairListC,pairHandP,pairHandC,blankcards)

    
            keys=[]

            for i in range(13):

                key = Button(gwin, Point(gridSlotsP[i][0]-10,gridSlotsP[i][1]),40,100, "")

                key.deactivate()

                key.setFill(color_rgb(60,179,113))

                keys.append(key)
                

            Deck= Image(Point(900,300),'playingcards/b1fv.gif')
            
            Deck.draw(gwin)
            


            #Deal the inital cards to the dealer and player
                
            game.initDeal(gwin)
            

            totalP= game.gettotal(pairHandP)

            TotalP1=Text(Point(900,360),"Player's Total:")

            TotalP1.draw(gwin)

            TotalP2=Text(Point(970,360),'0')

            TotalP2.setText(totalP)



            totalC= game.gettotal(pairHandC)

            TotalC1=Text(Point(900,240),"Computer's Total:")

            TotalC1.draw(gwin)

            TotalC2=Text(Point(980,240),'0')

            TotalC2.setText(totalC)

            
            # determine whos turn it is
            
            turn=game.whoStarts() #player= true///comp = false            

            

            if turn==True:   

                message=Text(Point(450,330),"""It's YOUR TURN! CLICK to start then, click on the card you wish

                             to ask the Comp for""")

                message.draw(gwin)

                

            elif turn==False:

                message=Text(Point(450,330),"It's the COMPUTER'S TURN first! CLICK to start")

                message.draw(gwin)

            pt=gwin.getMouse()

            
            

        #if the players hand is not empty and computers hand is not empty, and the deck is not empty

        

        elif len(pHand)!=0 and len(cHand)!=0 and game.isDeckEmpty()==False:



            #PLAYERS TURN  

            if turn==True:

                           

                print('your turn')

                #activate all the keys

                for i in range(len(pHand)):

                    keys[i].activate()

                    


                # number of pairs the player has
                indexPair = 0
                

                #the index of the card that the player picked in the keys list
                index = -1

                #boolean to determine if new game or exit is clicked
                keepPlaying = True


                #while the play gets a pair

                while indexPair !=None:
        


                    #have them choose a key

                    pt=gwin.getMouse()

                    #the index of the card that the player picked in the keys list
                    index = -1


                    # if they clicked new game or exit instead of choosing a card then break out of this while loop and perform those actions
                    
                    if newgameButton.clicked(pt)==True or exitButton.clicked(pt)==True:
                        
                        indexPair=None

                        keepPlaying = False
                        
                        print("clicked new button or  exit")

                    #if they did not click those buttons then let them keep playing  

                    if keepPlaying==True: 
                    
                        
                        #get the index of that key so can identify what rank it is

                        while index == -1 and keepPlaying==True:

                            for i in range(len(keys)):

                                if keys[i].clicked(pt)==True:

                                    index=i

                                    print(index,'index of card i ask for')

                                    break

                            # if they attempt to choose a card but fail to click in the right spot and they are prompted to pick another but
                            # they would rather just quit or start a new game
                            
                            if newgameButton.clicked(pt)==True or exitButton.clicked(pt)==True:
                        
                                indexPair=None

                                keepPlaying = False
                                
                                print("clicked new button or  exit")

                            # if they didn't click the exit or new game button and just clicked the wrong place that wasn't a valid card
                            
                            if keepPlaying ==True: 
                                
                                #let them know that they didn't pick a valid card and prompt them to try again
                                if index == -1 or index >= len(pHand):

                                    message.undraw()

                                    message=Text(Point(450,330),"You did not click a valid card, please try choosing a card again.")

                                    message.draw(gwin)

                                    pt=gwin.getMouse()                       

                                
                        #once they finally pick a valid card that they want to ask the computer for and they didn't click the exit or new game button
                                    
                        if keepPlaying == True: 

                            #if the player choose a valid card then check if that rank equals any cards in the computer's hand                    
                                
                            print('idx for pair check: ', index)

                            indexPair=game.checkPair(pHand[index],cHand)

        
                            #if there is a pair

                            if indexPair!= None:
                                

                                print(indexPair,'index of that card in comps hand')
                                

                                #put those cards into the pairList

                                pairHandP.append(pHand[index])

                                pairHandP.append(cHand[indexPair])

                                

                                #remove those cards from each other their hands


                                pHand.pop(index)

                                cHand.pop(indexPair)


                                #reset the buttons to activate the proper amount of buttons since the player will now have
                                #one less card
                                
                                #deactivate all the keys
                                

                                for i in range(len(keys)):

                                    keys[i].deactivate()


                                #now reactive only the ones you need
                                for i in range(len(pHand)):

                                    keys[i].activate()
                                 


                                #totals and prints the amount of pairs the player has 

                                totalP= game.gettotal(pairHandP)

                                TotalP2.setText(totalP)

                                TotalP2.undraw()

                                TotalP2.draw(gwin)

                                totalC= game.gettotal(pairHandC)

                                TotalC2.setText(totalC)

                                TotalC2.undraw()

                                TotalC2.draw(gwin)
                                

                                #lets the player know they got a match

                                message.undraw()

                                message=Text(Point(450,330),"CONGRATS you got match! Now pick another card to ask the computer for")

                                message.draw(gwin)

                                


                            #if there is not a pair, have the player go fish

                            else:

                                #print message for user 

                                message.undraw()

                                message=Text(Point(450,330),"Time to GO FISH!! The computer does not have that in their hand! ")

                                message.draw(gwin)

                                sleep(2)
                                

                                gotMatch = game.GoFishPlayer(gwin)
                                
        
                                # let the player know that they got a match on their draw

                                if gotMatch == True:
                                    
                                    message.undraw()

                                    message=Text(Point(450,330),"You got a match after you drew! It is now the computer's turn")

                                    message.draw(gwin)

                                    sleep(4)



                                #again totals the pairs just in case player got one when Going Fish 

                                totalP= game.gettotal(pairHandP)

                                TotalP2.setText(totalP)

                                TotalP2.undraw()

                                TotalP2.draw(gwin)

                                totalC= game.gettotal(pairHandC)

                                TotalC2.setText(totalC)

                                TotalC2.undraw()

                                TotalC2.draw(gwin)



                                #make sure that it knows that the player does NOT have any pairs

                                indexPair=None



                                                

                            #undraw all cards in comp hand

                            for i in range(len(imageListC)):

                                imageListC[i].undraw()

                            #undraws all the blanks

                            for i in range(len(blankcards)):
                                
                                blankcards[i].undraw()


                                 
                            

                            #undraw all cards in player

                            for i in range(len(imageListP)):

                                imageListP[i].undraw()

                            

                            

                            #redraws new hand without those cards and appends all those images to now empty image list. Also redraws all the pairs. 



                                #for comp

                            for i in range(len(cHand)):

                                imP=Image(Point(gridSlotsC[i][0],gridSlotsC[i][1]),'playingcards/'+ cHand[i].getSuit()+ str(cHand[i].getRank()) +'.gif')

                                imageListC.append(imP)

                                imP.draw(gwin)

                                fake = Image(Point(gridSlotsC[i][0],gridSlotsC[i][1]), 'playingcards/b1fv.gif')

                                blankcards.append(fake)

                                fake.draw(gwin)

                              

                            for i in range(len(pairHandC)):

                                imP=Image(Point(pairC[i][0],pairC[i][1]),'playingcards/'+ pairHandC[i].getSuit()+ str(pairHandC[i].getRank()) +'.gif')

                                pairListC.append(imP)

                                imP.draw(gwin)



                                # for player

                            for i in range(len(pHand)):

                                imP=Image(Point(gridSlotsP[i][0],gridSlotsP[i][1]),'playingcards/'+ pHand[i].getSuit()+ str(pHand[i].getRank()) +'.gif')

                                imageListP.append(imP)

                                imP.draw(gwin)

                                print(i)



                            for i in range(len(pairHandP)):

                                imP=Image(Point(pairP[i][0],pairP[i][1]),'playingcards/'+ pairHandP[i].getSuit()+ str(pairHandP[i].getRank()) +'.gif')

                                pairListP.append(imP)

                                imP.draw(gwin)                    




                            if len(pHand)==0 or len(cHand)==0:

                                indexPair  = None

                                print('here')

                                turn=False
                            
                                break
                            
                            

                #switches the turn to the computer

                print('sorry no match')

                turn=False       




            #COMPUTER'S TURN  

            elif turn==False:



                #deactivates all the players keys 

                for i in range(len(keys)):

                    keys[i].deactivate()



                #prints message for user    

                message.undraw()

                message=Text(Point(450,330),"It's the COMPUTER'S TURN!")

                message.draw(gwin)



                #the computer plays until they ask for a card that the player does not have. They then Go Fish 

                computerwin=game.DealerPlays(gwin)
                 



                #totals and prints the number of pairs the computer has 

                totalC= game.gettotal(pairHandC)

                print(totalC,'comp total')

                TotalC2.setText(totalC)

                TotalC2.undraw()

                TotalC2.draw(gwin)

                totalP= game.gettotal(pairHandP)

                print(totalP,'play total')

                TotalP2.setText(totalP)

                TotalP2.undraw()

                TotalP2.draw(gwin)

                int(totalC)
                
                int(totalP)

                if computerwin==-1:

                    
                    msg = ''
                    
                    if totalP > totalC:
                        
                        msg = "You WIN"
                        
                    elif totalP < totalC:
                        
                        msg = "You LOSE"
                        
                    else:
                        msg = "It was a TIE"
                        
                    message.undraw()
                    
                    print(msg)
                    
                    result = Text(Point(450,330), msg)
                    
                    result.draw(gwin)
                    
                    pt = gwin.getMouse()


                #prints message for user
                else:

                    message.undraw()

                    message=Text(Point(450,330),"It's YOUR TURN! CLICK on the card you wish to ask the Comp for")

                    message.draw(gwin)

                    #switches the turn to the player

                    turn=True


                

        #if the players hand=0 or the computers hand=0 or the deck does not have anymore cards, print the results of the game 

        elif len(pHand)==0 and len(cHand)==0 and game.isDeckEmpty()!=False:
            
            
            msg = ''
            
            if totalP > totalC:
                
                msg = "You WIN"
                
            elif totalP < totalC:
                
                msg = "You LOSE"
                
            else:
                
                msg = "It was a TIE"

                
                
            message.undraw()
            
            result = Text(Point(450,330),msg)
            
            result.draw(gwin)

      

            pt=gwin.getMouse() 

         
    gwin.close()  

    

main()























