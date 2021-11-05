import random

# Ik gebruik helaas globals dus alvast sorry

money = 25
weapon = False
parentsroad = False
BFFLucy = False
Yourself = False

def playAgain():
    global money
    global weapon
    global parentsroad
    global BFFLucy
    global Yourself
    print('Do you want to play again? (yes or no)')
    if input().lower().startswith('y'):
        money = 25
        weapon = False
        parentsroad = False
        BFFLucy = False
        Yourself = False
        start()
    elif input().lower().startswith('n'):
        exit()

def grocery():
    global parentsroad
    global BFFLucy
    global Yourself
    print("After working in the grocery store for a year you made enough money to buy a house.")
    if parentsroad == True:
        print("And after another year you made enough money to bring your parents over")
        print("3 years later you all live happely in the Netherlands.")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()
    elif BFFLucy == True:
        print("And after another year you made enough money to bring Lucy over")
        print("3 years later you both live happely in the Netherlands.")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()
    else:
        print("And after 5 years you found yourself a nice spouse and now live happely in the Netherlands")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()

def hardware():
    global parentsroad
    global BFFLucy
    global Yourself
    print("After working at the hardware store for while you bought yourself a house.")
    if parentsroad == True:
        print("And after another year you made enough money to bring your parents over")
        print("3 years later you all live happely in the Netherlands.")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()
    elif BFFLucy == True:
        print("And after another year you made enough money to bring Lucy over")
        print("3 years later you both live happely in the Netherlands.")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()
    else:
        print("And after 5 years you found yourself a nice spouse and now live happely in the Netherlands")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()

def army():
    global parentsroad
    global BFFLucy
    global Yourself
    print("After 4 years of training you oficialy joined the army.")
    if parentsroad == True:
        print("After another year you made enough money to bring your parents over")
        print("3 years later you all live happely in the Netherlands.")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()
    elif BFFLucy == True:
        print("After another year you made enough money to bring Lucy over")
        print("3 years later you both live happely in the Netherlands.")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()
    else:
        print("After 5 years you found yourself a nice spouse and now live happely in the Netherlands")
        print("Congratulations you safely made it all the way through the story!!")
        playAgain()

def NLwork():
    print("You arrive at the temp agency and they tell you there are 3 jobs available.")
    print("A. Grocery store employe 36 hours a week and you earn $2000 a month")
    print("B. Employe in a hardware store 38 hours and you earn $2200 a month")
    print("C. You could join the army and get a paid study you would earn $1000 a month")
    NLworkChoice = input("")
    if NLworkChoice == 'a':
        print("You decide to take a job by the grocery store.")
        grocery()
    elif NLworkChoice == 'b':
        print("You decide to take a job by the hardware store.")
        hardware()
    elif NLworkChoice == 'c':
        print("You decide to go for the army.")
        army()

def NederlandVluchtteling():
    print("You are brought to a fugitive camp to wait while they check if your story is true.")
    print("After a couple days they tell you your story check out.")
    print("After another half year you are told you can go out into society. What do you wanne do?")
    print("A. find a job.")
    print("B. write to people in your hometown")
    nederlander = input("")
    if nederlander == 'a':
        print("You go to a temp agency.")
        NLwork()
    elif nederlander == 'b':
        print("You write a letter to you family and friends about how you got to the Netherland and how you're doing.")
        print("After you asked someone to mail it you went to a temp agency to find a job.")
        NLwork()

def schiphol():
    print("The first thing you did when arriving at schiphol is that you wnet to the nearest police officer and told them you are a fugitive.")
    NederlandVluchtteling()

def planeride():
    print("You take your seat on the plane and wait for liftoff.")
    print("After half an hour the plane takes off and you look out the window at the place you leave behind.")
    print("Doesn't in look nice?")
    print("Anwser yes or no")
    planeride1 = input("")
    if planeride1 == 'yes':
        print("That was the only good part about it.")
        print("After a long planeride you arrive at schiphol.")
        schiphol()
    elif planeride1 == 'no':
        print("No everything about that place was bad.")
        print("After a long planeride you arrive at schiphol.")
        schiphol()

def work():
    ods = random.randint(0, 100)
    print("You decide to find a job to earn some money. After looking around you found 2 options.")
    print("A. You take job from the local gang")
    print("B. You decide to work a day on a construction site.")
    work1 = input("")
    if work1 == 'a':
        print("You decide to take the job from the gang.")
        print("They tell you you need to shoot some gang members on a construction site.")
        print("THey give you a gun and escort you to the construction site.")
        print("You gun down about 5 people before one of the construction worker grabs their gun and shoots you.")
        print("Sadly you have died.")
        playAgain()
    elif work1 == 'b'and ods <50:
        print("You arrive at your job and after an hour or so you see some people walk up to the the construction site.")
        print("Suddenly one of them grabs a gun and starts shooting people.")
        print("You try to take cover but you're just to late.")
        print("You have sadly bled out and died.")
        playAgain()
    elif work1 == 'b' and ods >=50:
        print("After about 6 hours of work you made enough money to buy the plane ticket.")
        print("You also heard that another construction site nearby had a shootout en a lot of people died.")
        print("Lucky for you that you worked on a different site.")
        print("You go back to the airport and buy a plane ticket.")
        planeride()

def SneakPlane():
    global parentsroad
    global BFFLucy
    global Yourself
    print("After an hour you see a plane to that is destined for the Netherlands.")
    print("You look around and don't see any personel.")
    print("You quickly move to towards the plane and try to get on it.")
    if parentsroad == True:
        print("You and your parents find a place to hide on the plane and wait.")
        print("After about an hour your hear people starting to load cargo onto the plane.")
        print("You tell your parents to be quiet and hope they don't find you...")
        print("After what seems like forever you see a pair of eyes looking at you and hear the man shout we got some hitchikers")
        print("The man runs out and calls the local airport police.")
        print("The police arrest you and your parents are all senticed to 5 years in jail.")
        print("This is where your story ends.")
        playAgain()
    elif BFFLucy == True:
        print("You and Lucy find a place to hide on the plane and wait.")
        print("After about an hour your hear people starting to load cargo onto the plane.")
        print("You tell Lucy to be quiet and hope they don't find you...")
        print("After what seems like forever you see a pair of eyes looking at you and hear the man shout we got some hitchikers")
        print("The man runs out and calls the local airport police.")
        print("The police arrest you and lucy you're both senticed to 5 years in jail.")
        print("This is where your story ends.")
        playAgain()
    elif Yourself == True:
        print("You find a place to hide on the plane and wait.")
        print("After about an hour your hear people starting to load cargo onto the plane.")
        print("After what seems like forever you see a pair of eyes looking at you and hear the man shout we got a hitchiker")
        print("The man runs out and calls the local airport police.")
        print("The police arrest you and you're senticed to 5 years in jail.")
        print("This is where your story ends.")
        playAgain()


def arrest():
    print("The police arrive at your location and tell them you need to come with them.")
    print("A. Follow their orders")
    print("B. Try to run away.")
    arrest1 = input("")
    if arrest1 == 'a':
        print("You follow them to the airport jail and they tell you to go in the cell.")
        print("After a hour they tell you you are summoned to court.")
        print("In the courtroom the judge tell you that you are beieng sued for the murder of a local shopkeeper.")
        print("They call up the leadwitness and Lucy walks up to the stand.")
        print("After a long trail you are found guilty of murder.")
        print("You have been sentenced for a life in prison for the murder of a shopkeeper.")
        print("Sadly this is were your story ends.")
        playAgain()
    elif arrest1 == 'b':
        print("The airport police taze you and lock you up.")
        print("You have been sentenced for a life in prison for the murder of a shopkeeper.")
        print("Sadly this is were your story ends.")
        playAgain()

def walk2():
    global money
    global parentsroad
    global BFFLucy
    global Yourself
    print("after 2 hours you arrive at the airport in kabul how do you plan on going on a plane. You currently have $"+str(money)+" in your wallet.")
    print("A. Buy one plane ticket (-$100)")
    print("B. Try and sneak onto on of the cargo planes")
    print("C. Go to kabul and try to make some money")
    planeride1 = input("")
    if planeride1 == 'a' and money >=100  and Yourself == True:
        print("You buy a plane ticket")
        money = money - 100
        planeride()
    elif planeride1 == 'a' and money >=100 and parentsroad == True:
        print("You buy a planeticket for yourself and promise your parents you will send them money so they can come later.")
        money = money - 100
        planeride()
    elif planeride1 == 'a' and money >=100 and BFFLucy == True:
        print("The moment you buy your ticket you see lucy talking to the local police.")
        print("You see them coming over to you.")
        arrest()
    elif planeride1 == 'a' and money  <100:
        print("You don't have enough money choice again.")
        walk2()
    elif planeride1 == 'b':
        print("You decide to try and sneak onto a plane. You quickly go into one of the personel exits.")
        SneakPlane()
    elif planeride1 == 'c':
        print("You decide to go to the city to find some work.")
        work()


def boothrobbery():
    global weapon
    global money
    print("You walk up to the booth to try and rob it what do you want do?")
    print("A. Tell him this is a robbery and he has to hand over the money and some food and drinks.")
    print("B. Threathen him with your kitchen knife")
    print("C. Stab him the kitchen knife")
    print("D. Continue on the road")
    booth1 = input("")
    if booth1 == 'b' and weapon == True:
        print("You grab your knife and threathen the shopkeeper. The shopkeepers grabs a shotgun and shoots you")
        print("Sadly you have died.")
        playAgain()
    elif booth1 == 'c' and weapon == True:
        print("You stab the shopkeeper and take find 100$ on him. You quickly cover your tacks and continue on your journey")
        money = money + 100
        walk2()
    elif booth1 == 'b' and weapon == False or booth1 == 'c' and weapon == False:
        print("You try to pull out a knife and find out you don't have one. You leave in shame.")
        walk2()
    elif str.lower(booth1) == 'a':
        print("The shopkeepers grabs a shotgun and shoots you")
        print("Sadly you have died.")
        playAgain()
    elif str.lower(booth1) == 'b':
        print("You continue on the road.")
        walk2()



def escapeplan():
    print("How do you want to leave the country")
    print("A. try to take a boat in Iran")
    print("B. try to take a plane")
    escapeplan1 = input("")
    if str.lower(escapeplan1) == 'a':
        print("You decide on trying to catch a boat.")
        boat()
    elif str.lower(escapeplan1) == 'b':
        print("You decide on trying to get on a plane.")
        plane()

def cab():
    global money
    print("You take a cab to the airport. The ride cost about $10.")
    money = money - 10
    walk2()


def walk():
    global money
    print("you started walking to the airport about 2 hours into the walk you see a little booth. What do you do?")
    print("A. Stop to buy some food and drinks for the road")
    print("B. continue on the road")
    print("C. try rob the booth to make some money for the plane ticket and to eat something")
    boothstory1 = input()
    if str.lower(boothstory1) == 'a':
        print("You spend 5$ and buy some food and drinks")
        money = money - 5
        walk2()
    elif str.lower(boothstory1) == 'b':
        print("You continue walking")
        walk2()
    elif str.lower(boothstory1) == 'c':
        print("You walk up to the booth how will you try to rob it?")
        boothrobbery()


def plane():
    print("Now that you decide on taking a plane you have to go there. How do you plan on getting there.")
    print("A. Walking there")
    print("B. getting a cab")
    print("C. try something else")
    planeQ1 = input()
    if str.lower(planeQ1) == 'a':
        print("You have decided on walking there.")
        walk()
    elif str.lower(planeQ1) == 'b':
        print("You have decided on getting a cab.")
        cab()
    elif str.lower(planeQ1) == 'c':
        print("You have decided on try something else.")
        escapeplan()

def NederlandPort():
    global money
    print("You have arrived in the Netherlands what do you wanne do first?")
    print("A. Go to the closest officer and tell them you're a fugitive")
    print("B. get something to eat you have $"+str(money)+" the food costs $4")
    NederlandPort1 = input("")
    if NederlandPort1 == 'a':
        print("You go and find a officer and tell them you're a fugitive")
        NederlandVluchtteling()
    elif NederlandPort1 == 'b' and money >=4:
        print("You buy a Frikandel and after eating you went to report that you're a fugitive")
        money = money - 4
        NederlandVluchtteling()
    elif NederlandPort1 == 'b' and money <4:
        print("You don't have enough money so you're gonna report that you are a fugitive")
        NederlandVluchtteling()

def storm():
    print("You sit on the boat for a long time and suddenly a horrible storm appears. What do you do?")
    print("A. Go outside and look what happens.")
    print("B. Stay where you are and hold on to your chair.")
    stormchoice = input("")
    if stormchoice == 'a':
        print("You decide to against logical thinking and go outside.")
        print("The moment you go outside the boat tilts and you lsoe your balance.")
        print("You fall overboard and try to get back on the boat.")
        print("Nothing works and you slowly lose conscious and drown.")
        print("Sadly you have died.")
        playAgain()
    elif stormchoice == 'b':
        print("You decide to stay inside and hold on to your chair for dear life.")
        print("After wat seems like forever the storms fades away.")
        print("After another hour you arrive in the Netherlands you safely made it.")
        NederlandPort()


def BoatTrip():
    global money
    print("You find a place to sit on the boat and look out the window waiting for the boat to leave.")
    print("After 10 min the boat departes the journey begins.")
    print("After 2 hours on the boat staff members come by and ask if you want something to eat and drink.")
    print("You currently have $"+str(money)+" in your wallet")
    print("A. You order somethin to eat and drink. cost $5")
    print("B. You tell them you don't need anything.")
    foodanddrinks = input("")
    if foodanddrinks == 'a' and money >=5:
        print("You some snacks and something to drink.")
        money = money - 5
        storm()
    elif foodanddrinks == 'a' and money <5:
        print("Sadly you don't have the money to buy it.")
        storm()
    elif foodanddrinks == 'b':
        print("You decide you don't need anything.")
        storm()

def cargosick():
    ods = random.randint(0, 100)
    if ods <70:
        print("You have succesfully made the trip to the Netherlands.")
        print("You sneak out of the boat before people check the cargo.")
        NederlandPort()
    elif ods >=70:
        print("You have fallen teribly ill")
        print("you look into the cargo and see it holds uranium.")
        print("You have died from radiantion poisoning.")
        playAgain()

def cargo():
    print("You are currently hiding with the cargo. The boat start to move do you want to change location?")
    print("A. Stay where I am")
    print("B. Move to where the passengers are")
    cargo1 = input("")
    if cargo1 == 'a':
        print("You stay where you are right now and continue on the journey.")
        cargosick()
    elif cargo1 == 'b':
        print("You get caught by on of the staff members.")
        print("They take you back to the port and hand you to the police.")
        print("You have been arrested and are sentenced to 1 year in jail")
        print("Sadly this is where our story for you ends")
        playAgain()

def sneakonboat():
    print("You have sneaked onto the boat but where are you gonna hide?")
    print("A. stay with the passengers")
    print("B. hide with the cargo")
    hideonboat = input("")
    if hideonboat == 'a':
        print("You blend in with the passengers and nobody questions you at the moment")
        BoatTrip()
    elif hideonboat == 'b':
        print("You hide with the cargo you're safe for now.")
        cargo()

def FindingABoat():
    global money
    global parentsroad
    global BFFLucy
    global Yourself
    print("After looking around for a bit you find a boat. You currently have $"+str(money)+" in your wallet.")
    print("A. Buy a boat ticket to the Netherlands (-$25)")
    print("B. Try and sneak onto the boat")
    boatride1 = input("")
    if boatride1 == 'a' and money >=25  and Yourself == True:
        print("You buy a boat ticket")
        money = money - 25
        BoatTrip()
    elif boatride1 == 'a' and money >=75 and parentsroad == True:
        print("You buy a boat ticket for you and your parents.")
        money = money - 75
        parentsroad = False
        BoatTrip()
    elif boatride1 == 'a' and money <75 and money >=25 and parentsroad == True:
        print("You buy a boat ride for yourself and promise your parents you will make money in the Netherlands to ship them over.")
        money = money - 25
        BoatTrip()
    elif boatride1 == 'a' and money >=50 and BFFLucy == True:
        print("You buy a plane ticket for you and Lucy.")
        money = money - 50
        BoatTrip()
    elif boatride1 == 'a' and money <50 and money >=25 and lucy == True:
        print("You buy a boat ride for yourself and promise Lucy you will make money in the Netherlands to ship her over.")
        money = money - 25
        BFFLucy = False
        BoatTrip()
    elif boatride1 == 'a' and money  <25:
        print("You don't have enough money choice again.")
        FindingABoat()
    elif boatride1 == 'b':
        print("You decide to try and sneak onto a boat. You wait for it to get dark and sneak aboard.")
        sneakonboat()

def port():
    global money
    print("You arrive at the port in Iran. what do you wanne do first.")
    print("A. Go and find a boat.")
    print("B. Go and sleep on a nearby bench.")
    port1 = input("")
    if port1 == 'a':
        print("You decide to look for a boat.")
        FindingABoat()
    elif port1 == 'b':
        ods = random.randint(0, 100)
        if ods <=50:
            print("You find a nice bench to take a nap on.")
            print("After waking up you decide to look for a boat.")
            FindingABoat()
        elif ods >50:
            print("While you were sleeping someone stole all your money.")
            print("You decide to try and find a boat anyways.")
            money = 0
            FindingABoat()


def boothrobberyForBoat():
    global weapon
    global money
    print("You walk up to the booth to try and rob it what do you want do?")
    print("A. Tell him this is a robbery and he has to hand over the money and some food and drinks.")
    print("B. Threathen him with your kitchen knife")
    print("C. Stab him the kitchen knife")
    print("D. Continue on the road")
    booth1 = input("")
    if booth1 == 'b' and weapon == True:
        print("You grab your knife and threathen the shopkeeper. The shopkeepers grabs a shotgun and shoots you")
        print("Sadly you have died.")
        playAgain()
    elif booth1 == 'c' and weapon == True:
        print("You stab the shopkeeper and take find 100$ on him. You quickly cover your tacks and continue on your journey")
        money = money + 100
        port()
    elif booth1 == 'b' and weapon == False or booth1 == 'c' and weapon == False:
        print("You try to pull out a knife and find out you don't have one. You leave in shame.")
        port()
    elif str.lower(booth1) == 'a':
        print("The shopkeepers grabs a shotgun and shoots you")
        print("Sadly you have died.")
        playAgain()
    elif str.lower(booth1) == 'b':
        print("You continue on the road.")
        port()

def RoadToTheBoat():
    global money
    print("After walking for about 2 hours you see a little booth. What do you do?")
    print("A. Stop to buy some food and drinks for the road")
    print("B. continue on the road")
    print("C. try rob the booth to make some money for the boat ride and to eat something")
    boothstory2 = input()
    if str.lower(boothstory2) == 'a':
        print("You spend 5$ and buy some food and drinks")
        money = money - 5
        port()
    elif str.lower(boothstory2) == 'b':
        print("You continue walking")
        port()
    elif str.lower(boothstory2) == 'c':
        print("You walk up to the booth how will you try to rob it?")
        boothrobberyForBoat()

def boat():
    global money
    print("You have decide to try and take a boat but how do you get there.")
    print("A. Walk there it takes about 4 hours so it will be night time when you arrive.")
    print("B. Take a cab")
    print("C. Try somethin else.")
    RoadToBoat = input("")
    if RoadToBoat == 'a':
        print("You decide to start walking there.")
        RoadToTheBoat()
    elif RoadToBoat == 'b':
        print("You decide to take a cab it takes about 40 minutes and cost $20")
        money = money - 20
        port()
    elif RoadToBoat == 'c':
        escapeplan()


def parents():
    print("You walk to your parents and tell them is time to escape and they agree with you but ask how do you plan on leaving?")
    print("A. try to take a boat in Iran")
    print("B. try to take a plane")
    parents1 = input("")
    if str.lower(parents1) == 'a':
        print("You and your parents decide to to take try and cath a boat")
        boat()
    elif str.lower(parents1) == 'b':
        print("You and your parent will try to go on a plane")
        plane()

def lucy():
    print("You walk to Lucy and tell her is time to escape and she agrees with you and asks how do we plan on leaving?")
    print("A. try to take a boat in Iran")
    print("B. try to take a plane")
    lucy1 = input("")
    if str.lower(lucy1) == 'a':
        print("You and Lucy decide to try and catch a boat")
        boat()
    elif str.lower(lucy1) == 'b':
        print("You and Lucy will try to get on a plane")
        plane()

def alone2():
    print("how do you plan on leaving the country?")
    print("A. try to take a boat in Iran")
    print("B. try to take a plane")
    alone3 = input("")
    if str.lower(alone3) == 'a':
        print("You decide to try and catch a boat")
        boat()
    elif str.lower(alone3) == 'b':
        print("You decide to try and get on a plane")
        plane()

def alone():
    print("Do you sneak out of the back of the house or go through the streets?")
    print("A. The back")
    print("B. the streets")
    alone1 = input("")
    if str.lower(alone1) == 'a':
        print("You sneak out of the back")
        alone2()
    elif str.lower(alone1) == 'b':
        print("You sneak past your parents and Lucy")
        alone2()

def street():
    global parentsroad
    global BFFLucy
    global Yourself
    print("You look out at the street and see your parent to the left and your best friend Lucy to the right. Where do you want to go?")
    print("A. To my parents")
    print("B. To my best friend Lucy")
    print("C. Try to sneak out alone")
    street1 = input("")
    if str.lower(street1) == 'a':
        print("You walk towards your parents")
        parentsroad = True
        parents()
    elif str.lower(street1) == 'b':
        print("You walk towards Lucy")
        BFFLucy = True
        lucy()
    elif str.lower(street1) == 'c':
        print("You Sneak out on your own")
        Yourself = True
        alone()

def start():
    global weapon
    print("You wake up in a cold dark bedroom and look around you seem to have forgoten who you are. You look down at yourself and see you are a...")
    print("A. a boy")
    print("B. a girl")
    print("C. Neither one of them")

    vraag1 = input("")

    if str.lower(vraag1) == 'a':
        print("Oh yes I am a boy. But what was my name again?")
    elif str.lower(vraag1) == 'b':
        print("Oh yes I am a girl. But what was my name again?")
    elif str.lower(vraag1) == 'c':
        print("Well there is no time for this. I have to figure out what my name is?")

    vraag2 = input("")

    if vraag2 not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a name.')

    print("oh yes I am "+vraag2+" now just to remember how old i am")

    vraag3 = input("")

    if vraag3 not in '0123456789':
             print('Please enter use numbers.')

    print("you remember now that you are a "+vraag3+" years old and living in Afganistan")

    print("last thing I remember was that I was trying to plan on escaping the country for somewhere save. but should I bring someone?")
    print("A. Bring my parents with me")
    print("B. Bring my best friend Lucy with me")
    print("C. go by myself")

    vraag4 = input("")

    if str.lower(vraag4) == 'a':
        print("then I should probably go and find the but where to look first")
        print("A. Try their bedroom")
        print("B. Go to the kitchen")
        print("C. Go out to the street")
        vraag5 = input("")
        if str.lower(vraag5) == 'a':
            print("You look in their bedroom and don't see them")
            print("A. look for them in the kitchen.")
            print("B. look for them on the streets.")
            sub1 = input("")
            if str.lower(sub1) == 'b':
                print("you decide to go to the streets")
                street()
            elif str.lower(sub1) == 'a':
                print("Well they are not in the kitchen do you want to grab some stuff before you go?")
                print("A. grab some stuff")
                print("B. no we are in a hurry")
                sub2 = input("")
                if str.lower(sub2) == 'b': 
                    print("you decide to go to the streets to find your parents.") 
                    street()
                elif str.lower(sub2) == 'a':
                    print("You grab some food and a knife and you go to the streets to find your parents.")
                    weapon = True
                    street()
        elif str.lower(vraag5) == 'b':
            print("Well they are not in the kitchen do you want to grab some stuff before you go?")
            print("A. grab some stuff")
            print("B. no we are in a hurry")
            vraag6 = input("")
            if str.lower(vraag6) == 'a':
                print("You grab some food and a knife.")
                weapon = True
                print("A. Look for them in their bedroom.")
                print("B. Go to the streets.")
                sub3 = input("")
                if str.lower(sub3) == 'a':
                    print("they are not in their bedroom so you decide to go to the streets")
                    street()
                elif str.lower(sub3) == 'b':
                    print("you decide to go to the streets")
                    street()
            elif str.lower(vraag6) == 'b':
                print("you decide to keep looking for your parents.") 
                print("A. go to the bedroom")
                print("B. go to the streets")
                sub4 = input("")
                if str.lower(sub4) == 'b':
                    print("you decide to go to the streets")
                    street()
                elif str.lower(sub4) == 'a':
                    print("They are not in de bedroom so you go to the streets.")
                    street()
        elif str.lower(vraag5) == 'c':
            print("You decide to go to the streets.")
            street()

    elif str.lower(vraag4) == 'b':
        print("You decide to go outside and look around to find lucy")
        street()
    elif str.lower(vraag4) == 'c':
        print("You decide to go by yourself and go to the street")
        street()

start()