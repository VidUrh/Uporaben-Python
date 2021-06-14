"""
Napisal:Vid Urh

Opomba: Projekt za učenje tkinter grafičnih orodij, izdelano v 1 letu učenja programiranja.

"""


from tkinter import * #Grafika
import random #Naključna izbira
import time
from PIL import Image, ImageTk



def Igra():
    class Zivali:
        def __init__(self,ime, mammal, carnivore, intervebrate, wild_cat, bird, horns, flying, water, stripes, colour):
            self.ime = ime
            self.mammal = mammal
            self.carnivore = carnivore
            self.intervebrate = intervebrate
            self.wild_cat = wild_cat
            self.bird = bird
            self.horns = horns
            self.flying = flying
            self.water = water
            self.stripes = stripes
            self.colour = colour
    
    tiger = Zivali('tiger', 'yes','yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'is orange')
    wolf = Zivali('wolf', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'can be grey, black or white')
    lion = Zivali('lion', 'yes', 'yes', 'no', 'yes', 'no','no', 'no', 'no', 'no', 'is gold/yellow')
    zebra = Zivali('zebra', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'is black and white')
    rattlesnake = Zivali('rattlesnake', 'no', 'yes', 'no', 'no', 'no', 'no','no','no','no', 'from light brown to grey')
    cobra = Zivali('cobra', 'no', 'yes', 'no', 'no', 'no', 'no','no','no','no', 'from light brown to grey')
    bee = Zivali('bee', 'no', 'no', 'yes','no', 'no', 'yes', 'yes', 'no', 'yes', 'is yellow and black')
    octopus = Zivali('octopus', 'no', 'yes', 'yes', 'no', 'no', 'no','no', 'yes', 'no', 'the colour is changeable')
    donkey = Zivali('donkey', 'yes', 'no', 'no,', 'no','no','no','no','no','no', 'can be grey, brown or black')
    eagle = Zivali('eagle','no', 'yes', 'no', 'no','yes','no', 'yes', 'no', 'no', 'is black with white head')
    penguin = Zivali('penguin', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'no', 'is black and white')
    fox = Zivali('fox', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'can be orange or red')
    sheep = Zivali('sheep', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'is white')
    goat = Zivali('goat', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'is brown')
    chicken = Zivali('chicken', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'from brown to gold')
    shark = Zivali('shark', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'white')
    dolphin = Zivali('dolphin', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'can be grey, black or white')
    duck = Zivali('duck', 'no','no','no','no','yes','no','yes','yes','no','can be brown,green and white')
    bear = Zivali('bear', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'can be grey, black, brown or white')
    bat = Zivali('bat', 'yes', 'yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'can be grey, black or brown')



    mozne_zivali = [tiger,wolf, lion, zebra, rattlesnake, cobra, bee, octopus, donkey, eagle, penguin, fox, sheep, goat, chicken, shark, dolphin, duck, bear, bat]
    izbrana_zival = random.choice(mozne_zivali)
    izbira = str(izbrana_zival.ime)
    


    class Welcome():  
        def __init__(self,master):
            barva_ozadja='#00FF66'
            
            self.master = master
            self.master.state("zoomed")
            self.master.title("Main menu")
            self.master['bg'] = barva_ozadja
            image = Image.open("mainlogo.jpg").resize((1366,768),Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            slikaz = Label(self.master,image=photo)
            slikaz.image = photo # keep a reference!
            slikaz.place(x=0, y=0, relwidth=1, relheight=1)
            
            label = Label(self.master,bg = barva_ozadja, text = 'CHOOSE A GAME MODE',font="Times 86 bold").place(relx = 0.5, anchor = N)
            button1 = Button(self.master, bg = '#00aa00', text = 'COMPUTER CHOOSES ANIMAL', font="Times 18 bold", command = self.Goto1).place(rely = 0.58, anchor = W)
            button2 = Button(self.master, bg = '#00aa00', text = 'YOU CHOOSE ANIMAL', font="Times 18 bold", command = lambda: self.Goto2()).place(rely = 0.58, relx = 0.99, anchor = E)
            exitbutton = Button(self.master, bg = '#00aa00', text = 'EXIT', font = "Times 18", width = 14, command = lambda: self.Exit()).place(rely = 0.99, relx = 0.99,anchor = SE)
            
        def Goto1(self):
            master1 = Tk()
            Gameplay1(master1)
            self.master.destroy()
    
        def Goto2(self):
                
            master2 = Tk()
            Gameplay2.master2 =master2
            self.master.destroy()
            Gameplay2(master2)
        def Exit(self):
            self.master.destroy()
            
            
    class SF():
        def __init__(self,stevilo):
            self.stevilo = stevilo
        
    
    class Gameplay1():
        stevilo = 0
        def __init__(self,master1):
            
            self.master1 = master1
            barva_ozadja = '#00FF66'
            visina_gumbov = 5
            razmik = 10
            stolpec3 = 2
            stolpec2 = 1
            stolpec = 0
            poravnava = W
            širina = 18
            barva_gumbov = '#00aa00'
            self.master1['bg'] = barva_ozadja
            self.master1.state("zoomed")
            self.master1.title("UGANI ŽIVAL")

            label = Label(self.master1, text = "COMPUTER ALREADY CHOSE \n GUESS THE ANIMAL", font = 'Times 36 bold',bg = barva_ozadja).place(relx = 0.5, anchor = N)
            label4= Label(self.master1, text = ' ', font = 'Times 72',bg = barva_ozadja).grid(columnspan = 2, row = 1)
            label2 = Label(self.master1, text = "POSSIBLE ANIMALS:", font = 'Times 24 bold', bg = barva_ozadja).grid(columnspan = 2, row = 2, pady = 25)
            label3 = Label(self.master1, text = 'HINTS:', font = 'Times 24 bold',bg = barva_ozadja).grid(columnspan = 2, column=3, row = 2, sticky = W)
    
            self.tiger = Button(self.master1, bg = barva_gumbov, text = 'TIGER', font = 'Times 14', command = lambda: self.PritisniNa(self.tiger,'tiger'))
            self.tiger.config(width = širina)
            self.tiger.grid(column = stolpec, row = 3, sticky = poravnava, pady = visina_gumbov, padx = razmik)
            
            self.wolf = Button(self.master1, bg = barva_gumbov, text = 'WOLF',font = 'Times 14', command = lambda: self.PritisniNa(self.wolf,'wolf'))
            self.wolf.config(width = širina)
            self.wolf.grid(column = stolpec,row =4, sticky = poravnava, pady = visina_gumbov, padx = razmik) 
    
            self.lion = Button(self.master1, bg = barva_gumbov, text = 'LION',font = 'Times 14', command = lambda: self.PritisniNa(self.lion, 'lion'))
            self.lion.config(width = širina)
            self.lion.grid(column = stolpec,row =5, sticky = poravnava, pady = visina_gumbov, padx = razmik) 
    
            self.zebra = Button(self.master1, bg = barva_gumbov,text = 'ZEBRA',font = 'Times 14', command = lambda: self.PritisniNa(self.zebra,'zebra'))
            self.zebra.config(width = širina)
            self.zebra.grid(column = stolpec,row = 6,sticky = poravnava, pady = visina_gumbov, padx = razmik) 
    
            self.rattlesnake = Button(self.master1, bg = barva_gumbov, text = 'RATTLESNAKE',font = 'Times 14', command = lambda: self.PritisniNa(self.rattlesnake,'rattlesnake'))
            self.rattlesnake.config(width = širina)
            self.rattlesnake.grid(column = stolpec,row = 7,sticky = poravnava, pady = visina_gumbov, padx = razmik) 
    
            self.cobra = Button(self.master1, bg = barva_gumbov,text = 'COBRA',font = 'Times 14', command = lambda: self.PritisniNa(self.cobra, 'cobra'))
            self.cobra.config(width = širina)
            self.cobra.grid(column = stolpec,row =8, sticky = poravnava, pady = visina_gumbov, padx = razmik) 
    
            self.bee = Button(self.master1, bg = barva_gumbov, text = 'BEE',font = 'Times 14', command = lambda: self.PritisniNa(self.bee,'bee'))
            self.bee.config(width = širina)
            self.bee.grid(column = stolpec,row =9, sticky = poravnava, pady = visina_gumbov, padx = razmik)

            self.octopus = Button(self.master1, bg = barva_gumbov,text = 'OCTOPUS',font = 'Times 14', command = lambda: self.PritisniNa(self.octopus,'octopus'))
            self.octopus.config(width = širina)
            self.octopus.grid(column = stolpec,row =10, sticky = poravnava, pady = visina_gumbov, padx = razmik)
    
            self.donkey = Button(self.master1, bg = barva_gumbov, text = 'DONKEY',font = 'Times 14', command = lambda: self.PritisniNa(self.donkey, 'donkey'))
            self.donkey.config(width = širina)
            self.donkey.grid(column = stolpec2,row =3, sticky = poravnava, pady = visina_gumbov, padx = razmik)
    
            self.eagle = Button(self.master1, bg = barva_gumbov,text = 'EAGLE',font = 'Times 14', command = lambda: self.PritisniNa(self.eagle,'eagle'))
            self.eagle.config(width = širina)
            self.eagle.grid(column = stolpec2,row =4, sticky = poravnava, pady = visina_gumbov, padx = razmik)
        
            self.penguin = Button(self.master1, bg = barva_gumbov, text = 'PENGUIN',font = 'Times 14', command = lambda: self.PritisniNa(self.penguin,'penguin'))
            self.penguin.config(width = širina)
            self.penguin.grid(column = stolpec2,row = 5,sticky = poravnava, pady = visina_gumbov, padx = razmik)

            self.fox = Button(self.master1, bg = barva_gumbov,text = 'FOX',font = 'Times 14', command = lambda: self.PritisniNa(self.fox,'fox'))
            self.fox.config(width = širina)
            self.fox.grid(column = stolpec2,row =6, sticky = poravnava, pady = visina_gumbov, padx = razmik)
            
            self.sheep = Button(self.master1, bg = barva_gumbov, text = 'SHEEP',font = 'Times 14', command = lambda: self.PritisniNa(self.sheep,'sheep'))
            self.sheep.config(width = širina)
            self.sheep.grid(column = stolpec2,row = 7,sticky = poravnava, pady = visina_gumbov, padx = razmik)
            
            self.goat = Button(self.master1, bg = barva_gumbov,text = 'GOAT',font = 'Times 14', command = lambda: self.PritisniNa(self.goat,'goat'))
            self.goat.config(width = širina)
            self.goat.grid(column = stolpec2,row = 8,sticky = poravnava, pady = visina_gumbov, padx = razmik)
            
            self.chicken = Button(self.master1, bg = barva_gumbov, text = 'CHICKEN',font = 'Times 14', command = lambda: self.PritisniNa(self.chicken,'chicken'))
            self.chicken.config(width = širina)
            self.chicken.grid(column = stolpec2,row = 9,sticky = poravnava, pady = visina_gumbov, padx = razmik)
    
            self.shark = Button(self.master1, bg = barva_gumbov,text = 'SHARK',font = 'Times 14', command = lambda: self.PritisniNa(self.shark,'shark'))
            self.shark.config(width = širina)
            self.shark.grid(column = stolpec2,row = 10,sticky = poravnava, pady = visina_gumbov, padx = razmik)

            self.dolphin = Button(self.master1, bg = barva_gumbov, text = 'DOLPHIN', font = 'Times 14', command = lambda: self.PritisniNa(self.dolphin,'dolphin'))
            self.dolphin.config(width = širina)
            self.dolphin.grid(column = stolpec3, row = 3, sticky = poravnava, pady = visina_gumbov, padx = razmik)

            self.duck = Button(self.master1, bg = barva_gumbov, text = 'DUCK', font = 'Times 14', command = lambda: self.PritisniNa(self.duck,'duck'))
            self.duck.config(width = širina)
            self.duck.grid(column = stolpec3, row = 4, sticky = poravnava, pady = visina_gumbov, padx = razmik)

            self.bear = Button(self.master1, bg = barva_gumbov, text = 'BEAR', font = 'Times 14', command = lambda: self.PritisniNa(self.bear,'bear'))
            self.bear.config(width = širina)
            self.bear.grid(column = stolpec3, row = 5, sticky = poravnava, pady = visina_gumbov, padx = razmik)


            self.bat = Button(self.master1, bg = barva_gumbov, text = 'BAT', font = 'Times 14', command = lambda: self.PritisniNa(self.bat,'bat'))
            self.bat.config(width = širina)
            self.bat.grid(column = stolpec3, row = 6, sticky = poravnava, pady = visina_gumbov, padx = razmik)
            

                  
    
        def PritisniNa(self, ime,imee):
            ime.config(state = 'disable')
            barva_ozadja = '#00FF66'
            self.stevilo = int(Sf.stevilo)
            if imee != izbira:
                if self.stevilo == 0:
                    if izbrana_zival.intervebrate == 'no':
                        hint1 = Label(self.master1,text = 'The secret animal is vertebrate', font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 3,  sticky = W)
                    if izbrana_zival.intervebrate == 'yes':
                        hint1 = Label(self.master1,text = 'The secret animal is intervebrate', font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 3,  sticky = W)

                elif self.stevilo == 1:
                    if izbrana_zival.mammal == 'yes':
                        hint2 =Label(self.master1, text ='The secret animal is mammal',font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 4, sticky = W)
                        
                    else:
                        hint2 =Label(self.master1, text = "The secret animal isn't mammal",font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 4,  sticky = W)
                elif self.stevilo == 2:
                    if izbrana_zival.bird == 'yes':
                        hint3 =Label(self.master1, text ='The secret animal is a bird',font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 5,  sticky = W)
                        
                    else:
                        hint3 =Label(self.master1, text = "The secret animal isn't a bird",font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 5,  sticky = W)
                elif self.stevilo == 3:
                    if izbrana_zival.carnivore == 'yes':
                        hint4 =Label(self.master1, text ='The secret animal is a carnivore',font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 6,  sticky = W)
                        
                    else:
                        hint4 =Label(self.master1, text = "The secret animal is a herbivore",font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 6,  sticky = W)
                elif self.stevilo == 4:
                    if izbrana_zival.horns == 'yes':
                        hint5 =Label(self.master1, text ='The secret animal has horns',font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 7,  sticky = W)
                        
                    else:
                        hint5 =Label(self.master1, text = "The secret animal doesn't have horns",font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 7,  sticky = W)
    
                elif self.stevilo == 5:
                    if izbrana_zival.wild_cat == 'yes':
                        hint6 =Label(self.master1, text ='The secret animal is a wild cat',font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 8,  sticky = W)
                        
                    else:
                        hint6 =Label(self.master1, text = "The secret animal isn't a wild cat",font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 8,  sticky = W)
                elif self.stevilo == 6:
                    if izbrana_zival.flying == 'yes':
                        hint7 =Label(self.master1, text ='The secret animal can fly',font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 9,  sticky = W)
                        
                    else:
                        hint7 =Label(self.master1, text = "The secret animal cannot fly",font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 9,  sticky = W)
                elif self.stevilo == 7:
                    if izbrana_zival.stripes == 'yes':
                        hint8 =Label(self.master1, text ='The secret animal has stripes',font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 10,  sticky = W)
                            
                    else:   
                        hint8 =Label(self.master1, text = "The secret animal doesn't have stripes",font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 10,sticky = W)
                elif self.stevilo == 8:
                    hint9 =Label(self.master1, text ='The colour of the secret animal ' + str(izbrana_zival.colour) ,font = 'Times 24', bg = barva_ozadja).grid(columnspan = 2, column=3, row = 11, sticky = W)
                elif self.stevilo == 9:
                        self.GotoEnd()
        
             
            else:
                self.GotoWin()
    
            self.stevilo+=1
            Sf.stevilo = self.stevilo
    
        def GotoWin(self):
            master3 = Tk()
            self.master1.destroy()
            Win(master3)
        def GotoEnd(self):
            master3 = Tk()
            self.master1.destroy()
            End(master3)
                        
            
            
            
       
           
    class End():
        def __init__(self,master3):
            self.master3 = master3
            barva_ozadja = '#00FF66'
            self.master3['bg'] = barva_ozadja
            self.master3.state("zoomed")
            self.master3.title("Lose")
            besedilo = 'The secret animal is ' + izbira 
            hint10 =Label(self.master3, text =besedilo.upper() ,font = 'Times 50', bg = '#FF0000').place(relx = 0.5, rely = 0.5, anchor = CENTER)
            mainmenubutton = Button(self.master3, bg = '#00aa00', text = 'Main menu', font = 'Times 14', command = lambda: self.GotoWelcome(self.master3)).place(relx = 0.9, rely = 0.9, anchor = SE)
            loselabel = Label(self.master3, text = 'You lost',font = 'Comic 44', bg = barva_ozadja).place(relx = 0.5, rely = 0.2, anchor = CENTER)

        def GotoWelcome(self,master3):
            self.master3.destroy()
            Igra()
    class Win():
        giftimer = 0
        def __init__(self,master3):
            self.master3 = master3
            barva_ozadja = '#00FF66'
            
            self.master3['bg'] = barva_ozadja
            self.master3.state("zoomed")
            self.master3.title("Win")
            zmagovalnlabel = Label(self.master3, text = 'You win',font = 'Comic 48', bg = barva_ozadja).place(relx = 0.5, rely = 0.5, anchor = CENTER)
            zmagovalnlabel2 = Label(self.master3, text = 'Congratulations',font = 'Comic 56', bg = barva_ozadja).place(relx = 0.5, rely = 0.2, anchor = CENTER)
            mainmenubutton = Button(self.master3, bg = '#00aa00', text = 'Main menu', font = 'Times 14', command = lambda: self.GotoWelcome(self.master3)).place(relx = 0.9, rely = 0.9, anchor = SE)
        
            
            self.CreateGif(self.master3)
        def CreateGif(self, master3):
            barva_ozadja = '#00FF66'
            stevilkaslike = 0
            while self.giftimer == 0:
                if self.giftimer == 0:
                    slika = "gif -index " + str(stevilkaslike)
                    gif = PhotoImage(file = 'Novo leto(gif).gif', format = slika)
                    giflabel = Label(master3, image = gif)
                    giflabel.image=gif
                    giflabel.place(relx=0.5, rely = 0.6, anchor = N)
                    giflabel.update()
                    time.sleep(0.02)
                    stevilkaslike += 1
                    if stevilkaslike == 61:
                        stevilkaslike = 0
            giftimer = 0
            return


        def GotoWelcome(self,master3):
            Win.giftimer += 1
            time.sleep(0.5)
            self.master3.destroy()
            Igra()
            
    
    class Gameplay2():
        question = 'IS YOUR ANIMAL MAMMAL?'
        barva_ozadja = '#00FF66'
        visina_gumbov = 5
        razmik = 10
        stolpec2 = 1
        stolpec = 0
        poravnava = W
        širina = 12
        def __init__(self,master2):
            self.vpr = StringVar(master2)

            barva_ozadja = self.barva_ozadja

            
            self.master2 = master2
            self.master2['bg'] = barva_ozadja
            self.master2.state("zoomed")
            self.master2.title("YOU CHOOSE")
            hint10 =Label(self.master2, text ='CHOOSE YOUR ANIMAL' ,font = 'Times 68', bg = '#FF0000').place(relx = 0.5, rely = 0.1, anchor = CENTER)
            labelzivali = Label(self.master2, text ='TIGER, WOLF, LION, ZEBRA, RATTLESNAKE, COBRA, BEE, OCTOPUS, DONKEY' ,font = 'Times 24', bg = barva_ozadja).place(relx = 0.5, rely = 0.22, anchor = CENTER)
            labelzivali2 = Label(self.master2, text ='EAGLE, PENGUIN, FOX, SHEEP, GOAT, CHICKEN, BEAR, DUCK, DOLPHIN, SHARK, BAT' ,font = 'Times 24', bg = barva_ozadja).place(relx = 0.5, rely = 0.3, anchor = CENTER)
            
            buttonyes = Button(self.master2, bg = '#00aa00', text = 'Yes',font = 'Times 24', command = lambda: self.setAnswertoYes(), width = self.širina).place(rely = 0.8, relx = 0.40, anchor = CENTER)
            buttonno = Button(self.master2, bg = '#00aa00', text = 'No',font = 'Times 24', command = lambda: self.setAnswertoNo(), width = self.širina).place(rely = 0.8, relx = 0.6, anchor = CENTER)
            self.questions = Label(self.master2, text = self.question,font = 'Times 24', bg = barva_ozadja)
            self.questions.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            vpr = self.vpr
            self.questions.wait_variable(vpr)
            if self.vpr.get() == 'no':
                self.askNextQuestionNoA()
                        
            elif self.vpr.get() == 'yes':
                self.askNextQuestionYesA()

        
               
        def setAnswertoNo(self):
            self.vpr.set('no')
        def setAnswertoYes(self):
            self.vpr.set('yes')
        def askNextQuestionYesA(self):
            vpr = self.vpr
            self.question ='IS YOUR ANIMAL CARNIVORE OR OMNIVORE?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)

            if 'yes' == self.vpr.get():
                self.askNextQuestionYesYesAB()
            elif 'no' == self.vpr.get():
                self.askNextQuestionYesNo()
        def askNextQuestionYesYesAB(self):
            vpr = self.vpr
            self.question ='DOES YOUR ANIMAL FLY?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A BAT'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' ==self.vpr.get():
               self.askNextQuestionYesYesA()

        def askNextQuestionYesYesA(self):
            vpr = self.vpr
            self.question ='DOES YOUR ANIMAL SWIM?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A DOLPHIN'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' ==self.vpr.get():
               self.askNextQuestionYesYes()

        def askNextQuestionNoA(self):
            vpr = self.vpr
            self.question = 'IS YOUR ANIMAL INTERVEBRATE?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)

            if 'yes'  == self.vpr.get():
                self.askNextQuestionNoYes()
            elif 'no' == self.vpr.get():
                self.askNextQuestionNoNo()
        def askNextQuestionYesYes(self):
            vpr = self.vpr
            self.question ='IS YOUR ANIMAL A WILD CAT?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.askNextQuestionYesYesYes()
            elif 'no' ==self.vpr.get():
               self.askNextQuestionYesYesNo()
        def askNextQuestionNoNo(self):
            vpr = self.vpr
            self.question ='IS YOUR ANIMAL A BIRD?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.askNextQuestionNoNoYes()
            elif 'no' == self.vpr.get():
               self.askNextQuestionNoNoNo()
        def askNextQuestionYesNo(self):
            vpr = self.vpr
            self.question ='IS YOUR ANIMAL A TYPE OF HORSE?'   
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.askNextQuestionYesNoNo()
            elif 'no' == self.vpr.get():
               self.askNextQuestionYesNoYes()
        def askNextQuestionNoNoYes(self):
            vpr = self.vpr
            self.question = 'DOES YOUR ANIMAL FLY?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
                self.askNextQuestionNoNoYesYes()
            elif 'no' == self.vpr.get():
                self.askNextQuestionNoNoYesNo()
        def askNextQuestionNoNoYesYes(self):
            vpr = self.vpr
            self.question = 'DOES YOUR ANIMAL SWIM?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A DUCK'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A EAGLE'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)

        def askNextQuestionNoYes(self):
            vpr = self.vpr
            self.question = 'DOES YOUR ANIMAL LIVE IN WATER?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS AN OCTOPUS'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A BEE'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
        def askNextQuestionYesYesYes(self):
            vpr = self.vpr
            self.question = 'DOES YOUR ANIMAL HAVE STRIPES?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A TIGER'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A LION'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
        def askNextQuestionNoNoNo(self):
            vpr = self.vpr
            self.question = 'IS YOUR ANIMAL A REPTILE?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.askNextQuestionNoNoNoNo()
            elif 'no' == self.vpr.get():
               self.question = 'YOUR ANIMAL IS A SHARK'
               self.questions.config(text = self.question)               
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)

        def askNextQuestionNoNoNoNo(self):
            vpr = self.vpr
            self.question = 'IS YOUR ANIMAL A COBRA?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question = 'YOUR ANIMAL IS A COBRA'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
               self.question = 'YOUR ANIMAL IS A RATTLESNAKE'
               self.questions.config(text = self.question)               
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
        def askNextQuestionNoNoYesNo(self):
            vpr = self.vpr
            self.question = 'IS YOUR ANIMAL SWIM?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A PENGUIN'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A CHICKEN'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
        def askNextQuestionYesYesNo(self):
            vpr = self.vpr
            self.question = 'IS YOUR ANIMAL BROWN?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A BEAR'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
               self.askNextQuestionYesYesNoNo()

        def askNextQuestionYesYesNoNo(self):
            vpr = self.vpr
            self.question = 'IS YOUR ANIMAL RED OR ORANGE?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A FOX'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A WOLF'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
        def askNextQuestionYesNoYes(self):
            vpr = self.vpr
            self.question = 'DOES YOUR ANIMAL HAVE WOOL?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
               self.question ='YOUR ANIMAL IS A SHEEP'
               self.questions.config(text = self.question)
               mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)
            elif 'no' == self.vpr.get():
                self.question ='YOUR ANIMAL IS A GOAT'
                self.questions.config(text = self.question)
                mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)


        def askNextQuestionYesNoNo(self):
            vpr = self.vpr
            self.question = 'DOES YOUR ANIMAL HAVE STRIPES?'
            self.questions.config(text = self.question)
            self.questions.wait_variable(vpr)
            if 'yes' == self.vpr.get():
                self.question ='YOUR ANIMAL IS A ZEBRA'
                self.questions.config(text = self.question)
                mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)

            elif 'no' == self.vpr.get():
                self.question ='YOUR ANIMAL IS A DONKEY'
                self.questions.config(text = self.question)
                mainmenubutton = Button(self.master2, bg = '#00aa00', text = 'Main Menu', font = 'Times 14', command = lambda: self.GotoWelcome()).place(relx = 0.9, rely = 0.9, anchor = SE)


        def GotoWelcome(self):
            self.master2.destroy()
            Igra()
            


    

    #print(izbira)
    Sf = SF(0)
    master = Tk()
    Welcome(master)
Igra()   
