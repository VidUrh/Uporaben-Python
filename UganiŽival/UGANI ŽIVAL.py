#DA GOVORI
#import pyttsx3
#DA TE RAZUME
#import speech_recognition as sr
#DA IZBERE NEKAJ NAKLJUČNO
import random
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# izbere eno žival
mozne_zivali = [tiger, wolf, lion, zebra, rattlesnake, cobra, bee, octopus, donkey, eagle, penguin, fox, sheep, goat, chicken]
izbrana_zival = random.choice(mozne_zivali)
a = str(izbrana_zival.ime)
# pozdravi in RAZLOŽI
def talkToMe(audio):
    print(audio)
    #engine.say(audio)
    #engine.runAndWait()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#odgovor
def myCommand():
    command = str(input()).lower()
    '''  r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print('OK')
        
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        
    except sr.UnknownValueError:
        talkToMe('Please repeat')
        command = myCommand();
    '''
    
    
    return command

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Razlaga ukazov
'''def askNextQuestionYesA():
    talkToMe('Is your animal carnivore?')
    command = myCommand()
    if 'yes' in command:
        askNextQuestionYesYes()
    elif 'no' in command:
        askNextQuestionYesNo()
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionYesA()
def askNextQuestionNoA():
    talkToMe('Is your animal invertebrate?')
    command = myCommand()
    if 'yes' in command:
        askNextQuestionNoYes()
    elif 'no' in command:
        askNextQuestionNoNo()
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionNoA()
def askNextQuestionYesYes():
    talkToMe('Is your animal a wild cat?')
    command = myCommand()
    if 'yes' in command:
       askNextQuestionYesYesYes()
    elif 'no' in command:
       askNextQuestionYesYesNo()
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionYesYes()
def askNextQuestionNoNo():
    talkToMe('Is your animal a bird?')
    command = myCommand()
    if 'yes' in command:
       askNextQuestionNoNoYes()
    elif 'no' in command:
       askNextQuestionNoNoNo()
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionNoNo()
def askNextQuestionYesNo():
    talkToMe('Does your animal have horns?')
    command = myCommand()
    if 'yes' in command:
       askNextQuestionYesNoYes()
    elif 'no' in command:
       askNextQuestionYesNoNo()
    else:
       talkToMe('Answer has to be YES or NO')
       askNextQuestionYesNo()
def askNextQuestionNoNoYes():
    talkToMe('Does your animal fly?')
    command = myCommand()
    if 'no' in command:
       askNextQuestionNoNoYesNo()
    elif 'yes' in command:
       talkToMe('Your animal is an eagle')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionNoNoYes()
def askNextQuestionNoYes():
    talkToMe('Is your animal live in water?')
    command = myCommand()
    if 'yes' in command:
       talkToMe('Your animal is an octopus')
    elif 'no' in command:
       talkToMe('Your animal is a bee')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionNoYes()
def askNextQuestionNoNoNo():
    talkToMe('Is your animal a cobra?')
    command = myCommand()
    if 'no' in command:
       talkToMe('Your animal is a rattlesnake')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionNoNoNo()
def askNextQuestionYesYesYes():
    talkToMe('Does your animal have stripes?')
    command = myCommand()
    if 'yes' in command:
       talkToMe('Your animal is a tiger.')
    elif 'no' in command:
       talkToMe('Your animal is a lion.')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionYesYesYes()
def askNextQuestionNoNoYesNo():
    command = myCommand()
    if 'yes' in command:
       talkToMe('Your animal is a penguin')
    elif 'no' in command:
       talkToMe('Your animal is a chicken')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionNoNoYesNo()
def askNextQuestionYesYesNo():
    talkToMe('Is your animal red or orange?')
    command = myCommand()
    if 'yes' in command:
       talkToMe('Your animal is a fox.')
    elif 'no' in command:
       talkToMe('Your animal is a wolf.')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionYesYesNo()
def askNextQuestionYesNoYes():
    talkToMe('Does your animal have wool?')
    command = myCommand()
    if 'yes' in command:
       talkToMe('Your animal is a sheep.')
    elif 'no' in command:
       talkToMe('Your animal is a goat.')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionYesNoYes()
def askNextQuestionYesNoNo():
    talkToMe('Does your animal have stripes?')
    command = myCommand()
    if 'yes' in command:
       talkToMe('Your animal is a zebra.')
    elif 'no' in command:
       talkToMe('Your animal is a donkey.')
    else:
        talkToMe('Answer has to be YES or NO')
        askNextQuestionYesNoNo()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ZAČNI
engine = pyttsx3.init()
engine.setProperty('rate',150)
talkToMe('HELLO DUDE!') # WE ARE GOING TO PLAY THE GAME! CHOOSE ONE OF THIS ANIMALS: TIGER, WOLF, LION, ZEBRA, RATTLESNAKE, COBRA, BEE, OCTOPUS, DONKEY, EAGLE, PENGUIN, FOX, SHEEP, GOAT, CHICKEN.')
talkToMe('I will ask questions and you answer with yes or no')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#razvrstitev
def assistant():
    talkToMe('Is your animal mammal?')
    command = myCommand()
    if 'yes' in command:
        askNextQuestionYesA()
    elif 'no' in command:
        askNextQuestionNoA()
    else:
        talkToMe('Answer has to be YES or NO')
        assistant()
        


assistant()
talkToMe('CONGRATULATIONS, YOU WON')'''
print('Guess the secret animal')
guess = myCommand()
if guess != a:
    if izbrana_zival.intervebrate == 'no':
        talkToMe('Next Hint\nThe secret animal is vertebrate\nNext guess')
    if izbrana_zival.intervebrate == 'yes':
        talkToMe('Next Hint\nThe secret animal is intervebrate\nNext guess')
    guess = myCommand()
    if guess != a:
        if izbrana_zival.mammal == 'yes':
            talkToMe('Next hint:\nThe secret animal is mammal\nNext guess')
        else:
            talkToMe("Next hint:\nThe secret animal isn't mammal\nNext guess")
        guess = myCommand()
        if guess != a:
            if izbrana_zival.bird == 'yes':
                talkToMe('Next hint:\nThe secret animal is a bird\nNext guess')
            else:
                talkToMe("Next hint:\nThe secret animal isn't a bird\nNext guess")
            guess = myCommand()
            if guess != a:
                if izbrana_zival.carnivore == 'yes':
                    talkToMe('Next hint:\nThe secret animal is a carnivore\nNext guess')
                else:
                    talkToMe("Next hint:\nThe secret animal isn't a carnivore\nNext guess")
                guess = myCommand()
                if guess != a:
                    if izbrana_zival.horns == 'yes':
                        talkToMe('Next hint:\nThe secret animal have horns\nNext guess')
                    else:
                        talkToMe("Next hint:\nThe secret animal doesn't have horns\nNext guess")
                    guess = myCommand()
                    if guess != a:
                        if izbrana_zival.wild_cat == 'yes':
                            talkToMe('Next hint:\nThe secret animal is a wild car\nNext guess')
                        else:
                            talkToMe("Next hint:\nThe secret animal isn't a wild cat\nNext guess")
                        guess = myCommand()
                        if guess != a:
                            if izbrana_zival.flying == 'yes':
                                talkToMe('Next hint:\nThe secret animal flies\nNext guess')
                            else:
                                talkToMe("Next hint:\nThe secret animal cannot fly\nNext guess")
                            guess = myCommand()
                            if guess != a:
                                if izbrana_zival.stripes == 'yes':
                                    talkToMe('Next hint:\nThe secret animal has stripes\nNext guess')
                                else:
                                    talkToMe("Next hint:\nThe secret animal doesn't have stripes\nNext guess")
                                guess = myCommand()
                                if guess != a:
                                    talkToMe('Next Hint\nThe colour of the secret animal ' + izbrana_zival.colour + '\nNext guess')
                                    guess = myCommand()
                                    if guess != a:
                                        print('The secret animal was:' + a + '\n You failed')
                                    else:
                                        print('success')
                                else:
                                    print('success')
                            else:
                                print('success')
                        else:
                            print('success')
                    else:
                        print('success')
                else:
                    print('success')
            else:
                print('success')
        else:
            print('success')
    else:
        print('success')

        
else:
    print('success')


#talkToMe('Next Hint\nThe colour of the secret animal ' + izbrana_zival.colour + '\nNext guess')














    
