#PWS

import math
import random

##############
#INSTELLINGEN#
##############
breukofheel = 0 #0 = geen breuken, 1 = breuken
soortvergelijking = 0 #0 = plus, 1 = min, 2 = keer, 3 = delen door

############
#PREPARATIE#
############
vergelijking = "" #strings
tussenantwoord1 = ""
tussenantwoord2 = ""
tussenantwoord3 = ""
eindantwoord = ""
voegwoord = ""
enofgeenen = ""
userinput = ""
linetoreplace = 0
sommenaanhetmaken = 0 #integers
tussenint1 = 0
tussenint2 = 0
tussenint3 = 0
tussenantwoorden = 0
goed1tussenstap = 0
goed2tussenstap = 0
fout1tussenstap = 0
fout2tussenstap = 0
foutinantwoord = 0
foutinstap2 = 0
foutinstap1 = 0
foutvolledigstap1 = 0
foutvolledigstap2 = 0
foutvolledigantwoord = 0
stappenovergeslagen = 0
sommengemaakt1tussenstap = 0
sommengemaakt2tussenstap = 0
finished = 0
hoeveelheidx = 0
incorrectheden = 0
b = 0
c = 0
d = 0
tussenint = 0

#################
#SOMMENGENERATOR#
#################
def sommengenerator():
    #we initialiseren wat globals, zodat deze niet als locals worden opgepikt
    global tussenantwoorden
    global vergelijking
    global eindantwoord
    global tussenantwoord1
    global tussenantwoord2
    global voegwoord
    global enofgeenen
    global sommengemaakt1tussenstap
    global sommengemaakt2tussenstap
    global hoeveelheidx
    global b
    global c
    global d
    global tussenint

    #deze uitgebreide randomising van getallen komt omdat python zijn random vaak op 0 eindigt
    b = random.randrange(21)
    c = random.randrange(21)
    d = random.randrange(21)

    if b == 0:
        b = random.randrange(21)

    if c == 0:
        c = random.randrange(21)

    if d == 0:
        d = random.randrange(21)

    #we randomisen meerdere keren omdat we anders vaak de zelfde vaste getallen krijgen
    if b == 0:
        b = random.randrange(21)

    if c == 0:
        c = random.randrange(21)

    if d == 0:
        d = random.randrange(21)

    #als laatste maatregel eerder genoemde vaste getallen
    if b == 0:
        b = 5

    if c == 0:
        c = 8

    if d == 0:
        d = 11

    
    hoeveelheidx = random.randrange(2) #0 of 1 x
    

    if soortvergelijking == 0 and breukofheel == 0:
        if hoeveelheidx == 0:
            tussenint = d - c
            tussenint1 = tussenint/b
            if abs(tussenint) > abs(b):
                tussenantwoord1 = str(b) + "x=" + str(tussenint)
                tussenantwoorden = tussenantwoorden + 1
                pastzovaakkomma = tussenint / b
                pnba = math.floor(abs(pastzovaakkomma))  # pnba = pastzovaaknaarbenedenafgerond
                if tussenint < 0:
                    pnba = - pnba
                if tussenint > 0:
                    pnba = pnba
                rest = abs(pastzovaakkomma - pnba) * b
                tussenantwoord2 = "x=" + str(tussenint) + "/" + str(b)
                tussenantwoorden = tussenantwoorden + 1
                if rest == 0:
                    if pastzovaakkomma > 0:
                        pastzovaakkomma = round(pastzovaakkomma)
                    elif pastzovaakkomma < 0:
                        pastzovaakkomma = round(pastzovaakkomma)
                        eindantwoord = "x=" + str(pastzovaakkomma)
                else:
                    eindantwoord = "x=" + str(pnba) + str(round(rest)) + "/" + str(b)
            elif abs(tussenint) == abs(b):
                tussenantwoord1 = str(b) + "x=" + str(tussenint)
                tussenantwoorden = tussenantwoorden + 1
                if tussenint < 0 and b > 0:
                    eindantwoord = "x=-1"
                if tussenint > 0 and b < 0:
                    eindantwoord = "x=-1"
                if tussenint < 0 and b < 0:
                    eindantwoord = "x=1"
                if tussenint > 0 and b > 0:
                    eindantwoord = "x=1"
            elif abs(tussenint) < abs(b):
                tussenantwoord1 = str(b) + "x=" + str(tussenint)
                tussenantwoorden = tussenantwoorden + 1
                if c == d:
                    eindantwoord = "x=0"
                else:
                    eindantwoord = "x=" + str(tussenint) + "/" + str(b)







        
        elif hoeveelheidx == 1: 
            tussenint = b + c 
            tussenantwoord1 = str(tussenint) + "x=" + str(d) 
            tussenantwoorden = tussenantwoorden + 1
            if abs(d) > abs(tussenint): 
                tussenantwoord2 = "x=" + str(d) + "/" + str(tussenint) 
                tussenantwoorden = tussenantwoorden + 1
                pastzovaakkomma = d / tussenint 
                pnba = math.floor(abs(pastzovaakkomma))  
                if tussenint < 0:
                    pnba = -pnba
                if tussenint > 0:
                    pnba = pnba
                    rest = abs(pastzovakkomma - pnba) * tussenint
                    tussenantwoord2 = "x=" + str(d) + "/" + str(tussenint)
                    tussenantwoorden = tussenantwoorden + 1
                    if rest == 0:
                        if pastzovakkomma > 0:
                            pastzovakkomma = round(pastzovakkomma)
                        elif pastzovakkomma < 0:
                            pastzovakkomma = round(pastzovakkomma)
                            eindantwoord = "x=" + str(pastzovakkomma)
                    else:
                        eindantwoord = "x=" + str(pnba) +  str(round(rest)) + "/" + str(tussenint)
            elif abs(d) == abs(tussenint):
                if tussenint < 0 and d > 0:
                    eindantwoord = "x=-1"
                if tussenint > 0 and d < 0:
                    eindantwoord = "x=-1"
                if tussenint < 0 and d < 0:
                    eindantwoord = "x=1"
                if tussenint > 0 and d > 0:
                    eindantwoord = "x=1"
            elif abs(d) < abs(tussenint): 
                eindantwoord = "x=" + str(d) + "/" + str(tussenint)

    # - vergelijking is aangepast met enofgeenen
    # - vergelijking is aangepast met wel of geen twee xen
    if tussenantwoorden == 1:
        voegwoord = "is"
        enofgeenen = "tussenantwoord"
        sommengemaakt1tussenstap = sommengemaakt1tussenstap + 1
    elif tussenantwoorden == 2 or tussenantwoorden == 0:
        voegwoord = "zijn"
        enofgeenen = "tussenantwoorden"
        sommengemaakt2tussenstap = sommengemaakt2tussenstap + 1
        
    if hoeveelheidx == 0:
        vergelijking = "Los de vergelijking " + str(b) + "x + " + str(c) + " = " + str(d) + " op. \nEr " + voegwoord + " " + str(tussenantwoorden) + "  " + enofgeenen + " nodig."
    elif hoeveelheidx == 1: #vergelijking met twee x'en
       vergelijking = "Los de vergelijking " + str(b) + "x + " + str(c) + "x" + " = " + str(d) + " op. \nEr " + voegwoord + " " + str(tussenantwoorden) + "  " + enofgeenen + " nodig." 
    # eind

###########
#INTERFACE#
###########
print("")
print ("U maakt momenteel gebruik van RuLuMaths versie 0.0.2.")
print ("Typ 'commands' voor een lijst met al de commands voor uw gebruik.")
print ("RuLuMaths gecreërd door Ruben Bogers en Luke van Dongen.")

#################
#NAKIJKENDE LOOP#
#################
while (finished) != 10:
    if sommenaanhetmaken == 0:
        userinput = input("\nInput: ")
        search = userinput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
        if search != -1:
            userinput = userinput.replace(' ','')
        if userinput == ("commands"):
            print ("Wat volgt is een lijst van mogelijke commands voor dit programma.")
            print ("Command 1 = commands, dit geeft een lijst van alle mogelijke commands weer.")
            print ("Command 2 = oefenen, hiermee start u een oefensessie.")
            print ("Command 3 = stop, hiermee verlaat u het programma.")
        elif userinput == ("oefenen"):
            sommengenerator()
            if breukofheel == 0:
                print("Soort getallen: gehele getallen")
            if soortvergelijking == 0:
                print("Soort vergelijking: optellen\n")
            elif soortvergelijking == 1:
                print("Soort vergelijking: aftrekken\n")
            elif soortvergelijking == 2:
                print("Soort vergelijking: vermenigvuldigen\n")
            elif soortvergelijking == 3:
                print("Soort vergelijking: delen\n")

            print(vergelijking)
            sommenaanhetmaken = 1
     
        elif userinput == ("stop"):
            print ("Je hebt het programma gestopt.")
            print ("Bedankt dat je vandaag met RuLuMaths hebt geoefend.")
            print ("Wij wensen u nog een fijne dag toe!")
            finished = 10
        else:
            print ("Je huidige input wordt niet herkend, gebruik 'commands' voor hulp")
    elif sommenaanhetmaken == 2:
        print ("\nWil je nog meer/verder oefenen?")
        print ("typ 'Ja' in als je verder wilt gaan, typ 'Nee' in als je wilt stoppen")
        userinput = input("\nVerdergaan: ")
        search = userinput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
        if search != -1:
            userinput = userinput.replace(' ','')
        if userinput == "Ja" or userinput == "JA" or userinput == "ja":
            tussenantwoorden = 0 #reset
            finished = 0 #reset
            sommengenerator()
            if breukofheel == 0:
                print("Soort getallen: gehele getallen")
            if soortvergelijking == 0:
                print("Soort vergelijking: optellen\n")
            elif soortvergelijking == 1:
                print("Soort vergelijking: aftrekken\n")
            elif soortvergelijking == 2:
                print("Soort vergelijking: vermenigvuldigen\n")
            elif soortvergelijking == 3:
                print("Soort vergelijking: delen\n")

            print(vergelijking)
            sommenaanhetmaken = 1
        elif userinput == "Nee" or userinput == "nee" or userinput == "NEE":
            sommenaanhetmaken = 0 #terug naar het hoofdmenu
    elif sommenaanhetmaken == 1:
        if tussenantwoorden == 0:
            if finished == 0:
                #deel 1: preparatie van de eerste input
                deelantwoordeninput = input("\nAntwoord: ")
                search = deelantwoordeninput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    deelantwoordeninput = deelantwoordeninput.replace(' ','')
                #deel 2: controle van de input
                if deelantwoordeninput == eindantwoord:
                    print("Correct, dit is het eindantwoord.\nLet echter wel op met het in één keer oplossen van de vergelijking, hiermee maak je snel simpele fouten.\nProbeer tussenstappen te maken om dze fouten te voorkomen.")
                    goed1tussenstap = goed1tussenstap + 1
                    sommenaanhetmaken = 2
                else:
                    if incorrectheden < 999:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout1tussenstap = fout1tussenstap + 1
                        foutinantwoord = foutinantwoord + 1
                   
        elif tussenantwoorden == 1:
            if finished == 0: #we zitten nog bij de eerste tussenstap
                #deel 1: preparatie van de eerste input
                deelantwoordeninput = input("\nTussenantwoord 1: ")
                search = deelantwoordeninput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    deelantwoordeninput = deelantwoordeninput.replace(' ','')
                #deel 2: controle van de input
                if deelantwoordeninput == tussenantwoord1:
                    print("Tussenantwoord 1 is correct")
                    finished = 1
                elif deelantwoordeninput == eindantwoord:
                    print("Correct, dit is het eindantwoord.\nLet echter wel op met het in één keer oplossen van de vergelijking, hiermee maak je snel simpele fouten.\nProbeer tussenstappen te maken om dze fouten te voorkomen.")
                    goed1tussenstap = goed1tussenstap + 1
                    stappenovergeslagen = stappenovergeslagen + 1
                    sommenaanhetmaken = 2
                else:
                    print("Incorrect, probeer het opnieuw.")
                    foutantwoord1 = deelantwoordeninput
                    foutantwoord2 = deelantwoordeninput
                    search = deelantwoordeninput.find("=")
                    if search != -1:
                        foutantwoord1 = deelantwoordeninput[search+1:]
                    search1 = deelantwoordeninput.find("x")
                    if search1 != -1:
                        foutantwoord2 = deelantwoordeninput[0:search1:]
                    if breukofheel == 0 and hoeveelheidx == 0 and deelantwoordeninput == str(b) + "x=" + str(c+d):
                        print("Feedback: Je hebt de constante waarden bij elkaar opgeteld, terwijl dit in dit geval niet de bedoeling is. Let op wat er gebeurt wanneer je een waarde naar de andere kant van de vergelijking brengt.")
                    elif breukofheel == 0 and hoeveelheidx == 0 and int(foutantwoord1) < tussenint:
                        print("Feedback: Je hebt een rekenfout gemaakt, je bent namelijk op een te lage waarde uit gekomen aan de rechterkant van de vergelijking.")
                    elif breukofheel == 0 and hoeveelheidx == 0 and int(foutantwoord1) > tussenint:
                        print("Feedback: Je hebt een rekenfout gemaakt, je bent namelijk op een te hoge waarde uit gekomen aan de rechterkant van de vergelijking.")
                    elif breukofheel == 0 and hoeveelheidx == 1 and deelantwoordeninput == str(b-c) + "x=" + str(d):
                        print("Feedback: Je hebt de x-waarden van elkaar afgetrokken, terwijl dit in dit geval niet de bedoeling is. Kijk goed naar de wiskundige symbolen.")
                    elif breukofheel == 0 and hoeveelheidx == 1 and int(foutantwoord2) < tussenint:
                        print("Feedback: Je hebt een rekenfout gemaakt, je bent namelijk op een te lage x-waarde uit gekomen aan de linkerkant van de vergelijking.")
                    elif breukofheel == 0 and hoeveelheidx == 1 and int(foutantwoord2) > tussenint:
                        print("Feedback: Je hebt een rekenfout gemaakt, je bent namelijk op een te hoge x-waarde uit gekomen aan de linkerkant van de vergelijking.")
            elif finished == 1: #het eindantwoord moet nu gegeven worden
                #deel 1: preparatie van de eerste input
                deelantwoordeninput = input("\nAntwoord: ")
                search = deelantwoordeninput.find(" ")
                if search != -1:
                    deelantwoordeninput = deelantwoordeninput.replace(' ','')
                #deel 2: controle van de input
                if deelantwoordeninput == eindantwoord:
                    print("Goedzo, je antwoord is correct")
                    goed1tussenstap = goed1tussenstap + 1
                    sommenaanhetmaken = 2
                else:
                    print("Incorrect, probeer het opnieuw.")
                    foutantwoord1 = deelantwoordeninput
                    foutantwoord2 = deelantwoordeninput.replace("-","") #hierbij wordt er niet naar het - teken gekeken
                    foutantwoord2 = foutantwoord2.replace(" ","")# opnieuw spaties vervangen
                    foutantwoord2 = foutantwoord2.replace("x=","") # hierbij kijkt hij over de x= heen
                  #  foutantwoord2 = foutantwoord2.replace("-","") 
                    search = deelantwoordeninput.find("=")
                    if search != -1:
                        foutantwoord1 = deelantwoordeninput[search+1:]
                    search1 = deelantwoordeninput.find("-")
                    if search1 != -1:
                        minteken = 1
                    else:
                        minteken = 0
                    search2 = deelantwoordeninput.find("1")
                    if search2 != -1:
                        eenofniet = 1
                    else:
                        eenofniet = 0
                    search3 = eindantwoord.find("-")
                    if search3 != -1:
                        minteken1 = 1
                    else:
                        minteken1 = 0
                        #eindantwoordfouten
                      #debug
                    print(foutantwoord2)
                    print(foutantwoord1)
					
                    ###############
					#foutenanalyse#
					###############
					
					if hoeveelheidx == 0:
						if abs(tussenint) > abs(b) and abs(rest) > 0 and str(foutantwoord2) != str(pnba) +  str(round(rest)) + "/" + str(tussenint):
							print("Feedback: Je hebt een rekenfout gemaakt. Let op je hoe vaak de deler geheel in het gedeelde getal past en hoeveel er dan overblijft in de deling.")
						elif abs(tussenint) > abs(b) and rest == 0 and str(foutantwoord2) != str(pastzovaakkomma):
							print("Feedback: Je hebt een rekenfout gemaakt. Let op er behoort bij deze deling een geheel getal zonder rest uit te komen.")
						elif abs(tussenint) == abs(b):
							if tussenint < 0 and b > 0 and minteken == 0:  #"x=-1"
								print("Feedback: Je bent een rekensymbool vergeten.")
							elif tussenint > 0 and b < 0 and minteken == 0:  #"x=-1"
								print("Feedback: Je bent een rekensymbool vergeten.")
							elif tussenint < 0 and b < 0 and minteken == 1:  #"x=1"
								print("Feedback: Je hebt een rekenfout gemaakt, je behoort hier namelijk niet op een negatieve waarde uit te komen.")
							elif tussenint > 0 and b > 0 and minteken == 1:  #"x=1"
								print("Feedback: Je hebt een rekenfout gemaakt, je behoort hier namelijk niet op een negatieve waarde uit te komen.")
							elif eenofniet == 0:
								print("Feedback: Je hebt een rekenfout gemaakt, je behoort hier namelijk op 1 of -1 uit te komen.")
						elif abs(tussenint) < abs(b):
						    elif c == d and str(foutantwoord2) != 0:
							    print("Feedback: Je hebt een rekenfout gemaakt. Wanneer je nul deelt door een getal krijg je altijd nul.")
						    elif str(foutantwoord2) != str(tussenint) + "/" + str(b):
							    print("Feedback: Je hebt een rekenfout gemaakt. Je behoort bij deze deling niet op rest uit te komen. Kijk goed of je de juiste getallen op de juiste manier hebt gebruikt in de deling.")
					elif hoeveelheidx == 1:
						if abs(d) > abs(tussenint) and abs(rest) > 0 and str(foutantwoord2) != str(pnba) +  str(round(rest)) + "/" + str(tussenint):
							print("Feedback: Je hebt een rekenfout gemaakt. Let op je hoe vaak de deler geheel in het gedeelde getal past en hoeveel er dan overblijft in de deling.")
						elif breukofheel == 0 and hoeveelheidx == 1 and abs(d) > abs(tussenint) and rest == 0 and str(foutantwoord2) != str(pastzovaakkomma):
							print("Feedback: Je hebt een rekenfout gemaakt. Let op er behoort bij deze deling een geheel getal zonder rest uit te komen.")
						elif breukofheel == 0 and hoeveelheidx == 1 and abs(d) == abs(tussenint):
							if tussenint < 0 and d > 0 and minteken == 0:  #"x=-1"
								print("Feedback: Je bent een rekensymbool vergeten.")
							elif tussenint > 0 and d < 0 and minteken == 0:  #"x=-1"
								print("Feedback: Je bent een rekensymbool vergeten.")
							elif tussenint < 0 and d < 0 and minteken == 1:  #"x=1"
								print("Feedback: Je hebt een rekenfout gemaakt, je behoort hier namelijk niet op een negatieve waarde uit te komen.")
							elif tussenint > 0 and d > 0 and minteken == 1:  #"x=1"
								print("Feedback: Je hebt een rekenfout gemaakt, je behoort hier namelijk niet op een negatieve waarde uit te komen.")
							elif eenofniet == 0:
								print("Feedback: Je hebt een rekenfout gemaakt, je behoort hier namelijk op 1 of -1 uit te komen.")
						elif abs(d) < abs(tussenint):
						    if str(foutantwoord2) != str(d) + "/" + str(tussenint):
							    print("Feedback: Je hebt een rekenfout gemaakt. Je behoort bij deze deling niet op rest uit te komen. Kijk goed of je de juiste getallen op de juiste manier hebt gebruikt in de deling.")
                       
                    #geldt voor hoeveelheidx = 0 or hoeveelheidx = 1
                    if hoeveelheidx == 0 or hoeveelheidx == 1 and abs(tussenint) != abs(b) and minteken1 == 0 and minteken == 1:
                        print("Feedback: Je bent op een negatieve waarde uitgekomen, wat met betrekking tot deze vergelijking niet klopt.")
                    elif hoeveelheidx == 0 or hoeveelheidx == 1 and abs(tussenint) != abs(b) and minteken1 == 1 and minteken == 0:
                        print("Feedback: Je bent op een positieve waarde uitgekomen, wat met betrekking tot deze vergelijking niet klopt.")


        
        elif tussenantwoorden == 2:
            if finished == 0:
                #deel 1: preparatie van de eerste input
                deelantwoordeninput = input("\nTussenantwoord 1: ")
                search = deelantwoordeninput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    deelantwoordeninput = deelantwoordeninput.replace(' ','')
                    
                #deel 2: controle van de input
                if deelantwoordeninput == tussenantwoord1:
                    print("Tussenantwoord 1 is correct")
                    finished = 1
                elif deelantwoordeninput == tussenantwoord2:
                    print("correct, je hebt wel hebt een tussenantwoord overgeslagen, probeer voortaan alle tussenantwoorden uit te werken")
                    finished = 2 #direct door naar eindantwoord
                    stappenovergeslagen = stappenovergeslagen + 1
                elif deelantwoordeninput == eindantwoord:
                    print("Correct, dit is het eindantwoord.\nLet echter wel op met het in één keer oplossen van de vergelijking, hiermee maak je snel simpele fouten.\nProbeer tussenstappen te maken om dze fouten te voorkomen.")
                    sommenaanhetmaken = 2
                    goed2tussenstap = goed2tussenstap + 1
                    stappenovergeslagen = stappenovergeslagen + 1
                else:
                    if incorrectheden < 999:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout2tussenstap = fout2tussenstap + 1
                        foutinstap1 = foutinstap1 + 1
                    else:
                        print("Nogsteeds incorrect, de juiste stap was: " + str(tussenantwoord1) + " probeer de tweede tussenstap te geven")
                        incorrectheden = 0 #reset
                        finished = 1
                        foutvolledigstap1 = foutvolledigstap1 + 1
                        fout2tussenstap = fout2tussenstap + 1
                        foutinstap1 = foutinstap1 + 1
            elif finished == 1:
                #deel 1: preparatie van de eerste input
                deelantwoordeninput = input("\nTussenantwoord 2: ")
                search = deelantwoordeninput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    deelantwoordeninput = deelantwoordeninput.replace(' ','')
                    
                #deel 2: controle van de input
                if deelantwoordeninput == tussenantwoord2:
                    print("Tussenantwoord 2 is correct")
                    finished = 2
                elif deelantwoordeninput == eindantwoord:
                    print("Je hebt het eindantwoord gegeven, dit is correct, maar probeer in de toekomst eerst de tussenstappen te geven")
                    sommenaanhetmaken = 2
                    goed2tussenstap = goed2tussenstap + 1
                    stappenovergeslagen = stappenovergeslagen + 1
                else:
                    if incorrectheden < 999:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout2tussenstap = fout2tussenstap + 1
                        foutinstap2 = foutinstap2 + 1
            elif finished == 2:
                #deel 1: preparatie van de eerste input
                deelantwoordeninput = input("\nAntwoord: ")
                search = deelantwoordeninput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    deelantwoordeninput = deelantwoordeninput.replace(' ','')
                #deel 2: controle van de input
                if deelantwoordeninput == eindantwoord:
                    print("Je eindantwoord is correct, goed bezig!")
                    sommenaanhetmaken = 2
                    goed2tussenstap = goed2tussenstap + 1
                else:
                    if incorrectheden < 999:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout2tussenstap = fout2tussenstap + 1
                        foutinantwoord = foutinantwoord + 1
