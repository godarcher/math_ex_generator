# -*- coding: cp1252 -*-
#PWS

import math
import random
import datetime

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
incorrectheden = 0

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

    #josso nieuwe code begin
    hoeveelheidx = random.randrange(2) #0 of 1 x
    #josso nieuwe code eind

    if soortvergelijking == 0 and breukofheel == 0:
        if hoeveelheidx == 0: #oude stuk - josso
            tussenint = d - c #-11
            tussenint1 = tussenint/b
            #josso debug - voor 1x is de som natuurlijk anders
            if b == 1:
                eindantwoord = "x=" + str(tussenint)
            #josso debug einde
            elif abs(tussenint) > abs(b): #11 > 8
                tussenantwoord1 = str(b) + "x=" + str(tussenint)
                tussenantwoorden = tussenantwoorden + 1
                pastzovaakkomma = tussenint / b #-11/8 
                pnba = math.floor(abs(pastzovaakkomma))  # pnba = pastzovaaknaarbenedenafgerond
                if tussenint < 0:
                    pnba = - pnba #pnba = -1
                if tussenint > 0:
                    pnba = pnba
                    
                #debug josso - er gaat hier iets fout bij de rest  
                    #3x = 10
                    #x = 10/3
                    #pastzovaakabs = 3
                    #rest = noemer - 3 * deler
                restberekenaar = b * pnba #-8
                rest = abs(tussenint) - abs(restberekenaar) #11 - 8 = 3
                #debug josso - einde
                
                tussenantwoord2 = "x=" + str(tussenint) + "/" + str(b)
                tussenantwoorden = tussenantwoorden + 1
                if rest == 0:
                    #debug josso 2.0 - we moeten hier ook nog de float (2.0) naar een int compensenseren
                    pastzovaakcompensated = str(pastzovaakkomma)
                    search = pastzovaakcompensated.find(".") #we kunnen punten alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                    if search != -1:
                        strlength = len(pastzovaakcompensated) #lengte van de string
                        strlength = strlength - 2 #laatste twee digits
                        pastzovaakcompensated = str(pastzovaakcompensated)[0:strlength] #we snijden twee digits eraf
                    #debug josso 2.0 - einde
                    eindantwoord = "x=" + pastzovaakcompensated
                else:
                    #debug josso 3.0 - we moeten hier ook nog de float (2.0) naar een int compensenseren
                    pnbacompensated = str(pnba)
                    search = pnbacompensated.find(".") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                    if search != -1:
                        strlength = len(pnbacompensated) #lengte van de string
                        strlength = strlength - 2 #laatste twee digits
                        pnbacompensated = str(pnbacompensated)[0:strlength] #we snijden twee digits eraf
                    #debug josso 3.0 - einde

                    #debug josso 4.0 - we moeten ook hier de float van rest naar een int compenseren
                    restcompensated = str(abs(rest))
                    search = restcompensated.find(".") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                    if search != -1:
                        strlength = len(restcompensated) #lengte van de string
                        strlength = strlength - 2 #laatste twee digits
                        restcompensated = str(restcompensated)[0:strlength] #we snijden twee digits eraf
                    #debug josso 4.0 eind
                    eindantwoord = "x=" + pnbacompensated + restcompensated + "/" + str(b)
            elif abs(tussenint) == abs(b):
                tussenantwoord1 = str(b) + "x=" + str(tussenint)
                tussenantwoorden = tussenantwoorden + 1
                #debug josso 5.0 - we moeten ook hier de float van tussenint naar een int compenseren
                tussenintcompensated = str(tussenint1)
                search = tussenintcompensated.find(".") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    strlength = len(tussenintcompensated) #lengte van de string
                    strlength = strlength - 2 #laatste twee digits
                    tussenintcompensated = str(tussenintcompensated)[0:strlength] #we snijden twee digits eraf
                eindantwoord = "x=" + str(tussenintcompensated)
            elif abs(tussenint) < abs(b):
                tussenantwoord1 = str(b) + "x=" + str(tussenint)
                tussenantwoorden = tussenantwoorden + 1
                if c == d:
                    eindantwoord = "x=0"
                else:
                    eindantwoord = "x=" + str(tussenint) + "/" + str(b)
        #nieuwe code josso begin (twee x'en optelsom)
        elif hoeveelheidx == 1: 
            tussenint = b + c #3x + 10x = 20, tussenint = 13
            tussenantwoord1 = str(tussenint) + "x=" + str(d) #13x = 20
            tussenantwoorden = tussenantwoorden + 1
            if d > tussenint: #13x = 20
                tussenantwoord2 = "x=" + str(d) + "/" + str(tussenint) #x = 20/13
                tussenantwoorden = tussenantwoorden + 1
                
                pastzovaakkomma = d / tussenint #1.nogwat
                pnba = math.floor(abs(pastzovaakkomma))  #1
                restberekenaar = tussenint * pnba #1 * 13 = 13
                rest = d - abs(restberekenaar) #7

                pnbacompensated = str(pnba)
                search = pnbacompensated.find(".") #we kunnen punten alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    strlength = len(pnbacompensated) #lengte van de string
                    strlength = strlength - 2 #laatste twee digits
                    pnbacompensated = str(pnbacompensated)[0:strlength] #we snijden twee digits eraf

                restcompensated = str(rest)
                search = restcompensated.find(".") #we kunnen punten alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    strlength = len(restcompensated) #lengte van de string
                    strlength = strlength - 2 #laatste twee digits
                    restcompensated = str(restcompensated)[0:strlength] #we snijden twee digits eraf

                if rest > 0:
                    eindantwoord = "x=" + pnbacompensated + restcompensated + "/" + str(tussenint) #x = 1 7/13
                elif rest == 0:
                    eindantwoord = "x=" + pnbacompensated
            elif d == tussenint: #20x = 20
                eindantwoord = "x=1"
            elif d < tussenint: #20x = 13
                eindantwoord = "x=" + str(d) + "/" + str(tussenint) #x = 13/20
        #nieuwe code josso einde 


    #josso - vergelijking is aangepast met enofgeenen
    #josso - vergelijking is aangepast met wel of geen twee xen
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
    #josso eind
#onze functie eindight hier

def lijnenvervanger(my_file, replacement):
    global linetoreplace
    with open(my_file, "r") as file:
         lines = file.readlines() #array van lijnen verkregen

    if len(lines) > int(linetoreplace):
         lines[linetoreplace] = replacement

    with open(myfile, "w") as file:
        file.writelines( lines )

    linetoreplace = linetoreplace + 1 #elke keer de volgende lijn

###########
#INTERFACE#
###########
print(tosay)
print("")
print "U maakt momenteel gebruik van CyberMath versie 0.0.1"
print "Huidige datum en tijd: " + now.strftime("%Y-%m-%d %H:%M")
print "Typ 'cmds' voor een lijst inputs om te gebruiken"
print "CyberMath haar scheppers zijn Luke en Ruben"

#################
#NAKIJKENDE LOOP#
#################
while (finished) != 10:
    if sommenaanhetmaken == 0:
        userinput = input("\nInput: ")
        search = userinput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
        if search != -1:
            userinput = userinput.replace(' ','')
        if userinput == ("cmds"):
            print "Wat volgt is een lijst mogelijke inputs voor de computer"
            print "Command 1 = cmds, dit geeft een lijst van alle inputs weer"
            print "Command 2 = oefenen, hiermee start u een oefensessie"
            print "Command 3 = statistiek.sessie, voor data van huidige sessie"
            print "Command 4 = statistiek.dag, voor data van vandaag"
            print "Command 5 = statistiek.all, voor totale data"
            print "Command 6 = analyse.sessie, voor analyse van huidige sessie"
            print "Command 7 = analyse.dag, voor analyse van vandaag"
            print "Command 8 = analyse.all, voor totale data"
            print "Command 9 = stop, hiermee verlaat u het programma"
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
        elif userinput == ("statistiek.sessie"):
            print "STATISTIEK VAN HUIDIGE SESSIE"
            #blok 1: berekeningen
            aantalsommen = sommengemaakt1tussenstap + sommengemaakt2tussenstap
            #blok 2: databombardement
            print "sommen gemaakt = " + str(aantalsommen)
            print "sommen gemaakt met 1 tussenstap = " + str(sommengemaakt1tussenstap)
            print "sommen gemaakt met 2 tussenstappen = " + str(sommengemaakt2tussenstap)
            print ""
            print "aantal sommen met 1 tussenstap goed = " + str(goed1tussenstap)
            print "aantal sommen met 2 tussenstappen goed = " + str(goed2tussenstap)
            print "aantal fouten bij sommen met 1 tussenstap = " + str(fout1tussenstap)
            print "aantal fouten bij sommen met 2 tussenstappen = " + str(fout2tussenstap)
            print ""
            print "aantal fouten gemaakt bij het geven van tussenstap 1 = " + str(foutinstap1)
            print "aantal fouten gemaakt bij het geven van tussenstap 2 = " + str(foutinstap2)
            print "aantal fouten gemaakt bij het geven van een eindantwoord = " + str(foutinantwoord)
            print ""
            print "aantal tussenstappen 1 veelvoudig fout gedaan = " + str(foutvolledigstap1) 
            print "aantal tussenstappen 2 veelvoudig fout gedaan = " + str(foutvolledigstap2)
            print "aantal eindantwoorden veelvoudig fout gedaan = " + str(foutvolledigantwoord)
            print ""
            print "aantal stappen overgeslagen = " + str(stappenovergeslagen)
        elif userinput == ("analyse.sessie"):
            print "ANALYSE VAN HUIDIGE SESSIE"
            sommengemaakt = sommengemaakt1tussenstap + sommengemaakt2tussenstap
            #deel 1: inschatting betrouwbaarheid analyse
            if sommengemaakt < 10 or sommengemaakt == 10:
                print("Voor een analyse heb je eigenlijk meer data nodig dan de " + str(sommengemaakt) + " sommen die je vandaag hebt gemaakt")
            elif sommengemaakt > 10  and sommengemaakt < 25:
                print("Analysebetrouwbaarheid bij " + str(sommengemaakt) + " gemaakte sommen = redelijk betrouwbaar")
            elif sommengemaakt > 25 or sommengemaakt == 25:
                print("Analysebetrouwbaarheid bij " +  str(somemngemaakt) + " gemaakte sommen = zeer betrouwbaar")
            #deel 2: zwakke en goede punten
            if sommengemaakt1tussenstap != 0 and sommengemaakt2tussenstap != 0:
                foutpersom1t = float(fout1tussenstap) / float(sommengemaakt1tussenstap)
                foutpersom2t = float(fout2tussenstap) / float(sommengemaakt2tussenstap)
                if foutpersom2t > foutpersom1t:
                    print("Je maakt vooral fouten bij sommen met twee tussenstappen, je hebt hier een fout per som ratio van: " + str(foutpersom2t))
                    print("Bij sommen met een tussenstap is je fout per som ratio lager, namelijk: " + str(foutpersom1t))
                elif foutpersom2t < foutpersom1t:
                    print("Je maakt vooral fouten bij sommen met een tussenstappen, je hebt hier een fout per som ratio van: " + str(foutpersom1t))
                    print("Bij sommen met twee tussenstappen is je fout per som ratio lager, namelijk: " + str(foutpersom2t))
                if foutpersom1t > 0.20:
                    print("Je maakt nog teveel fouten per som bij sommen met een tussenstap, oefen deze vaker of vraag je leraar om tips")
                if foutpersom2t > 0.20:
                    print("Je maakt nog teveel fouten per som bij sommen met twee tussenstappen, oefen deze vaker of vraag je leraar om tips")

                stapfout1pergeheel = float(foutinstap1) / float(sommengemaakt)
                stapfout2pergeheel = float(foutinstap2) / float(sommengemaakt2tussenstap)
                stapfoutepergeheel = float(foutinantwoord) / float(sommengemaakt)
                if stapfout1pergeheel > stapfout2pergeheel and stapfout1pergeheel > stapfoutepergeheel:
                    print("Je maakt vooral fouten in de eerste stap van een som, je hebt hier een fout per stap ratio van: " + str(stapfout1pergeheel))
                    print("In de tweede stap van de som maak je relatief minder fouten, namelijk een fout per stap ratio van: " + str(stapfout2pergeheel))
                    print("Ook in je antwoord maak je relatief minder fouten, namelijk een fout per stap ratio van: " + str(stapfoutepergeheel))
                elif stapfout2pergeheel > stapfout1pergeheel and stapfout2pergeheel > stapfoutpergeheel:
                    print("Je maakt vooral fouten in de tweede stap van een som, je hebt hier een fout per stap ratio van: " + str(stapfout2pergeheel))
                    print("In de eerste stap van de som maak je relatief minder fouten, namelijk een fout per stap ratio van: " + str(stapfout1pergeheel))
                    print("Ook in je antwoord maak je relatief minder fouten, namelijk een fout per stap ratio van: " + str(stapfoutepergeheel))
                elif stapfoutepergeheel > stapfout1pergeheel and stapfoutepergeheel > stapfout2pergeheel:
                    print("Je maakt vooral fouten in het eindantwoord van de som, je hebt hier een fout per stap ratio van: " + str(stapfoutepergeheel))
                    print("In de eerste stap van de som maak je relatief minder fouten, namelijk een fout per stap ratio van: " + str(stapfout1pergeheel))
                    print("Ook in de tweede stap maak je relatief minder fouten, namelijk een fout per stap ratio van: " + str(stapfout2pergeheel))
                if stapfout1pergeheel > 0.20:
                    print("Je maakt nog teveel fouten in de eerste tussenstap van een som oefen deze vaker of vraag je leraar om tips")
                if stapfout2pergeheel > 0.20:
                    print("Je maakt nog teveel fouten in de tweede tussenstap van een som oefen deze vaker of vraag je leraar om tips")
                if stapfoutepergeheel > 0.20:
                    print("Je maakt nog teveel fouten in het definitieve antwoord van je som oefen deze vaker of vraag je leraar om tips")

                stap1volledigpergeheel = float(foutvolledigstap1) / float(sommengemaakt)
                stap2volledigpergeheel = float(foutvolledigstap2) / float(sommengemaakt2tussenstap)
                stapevolledigpergeheel = float(foutvolledigantwoord) / float(sommengemaakt)
                if stap1volledigpergeheel > 0.08:
                    print("Je hebt de eerste stap van een som nog te vaak volledig fout, oefen deze vaker of vraag je leraar om tips")
                if stap2volledigpergeheel > 0.08:
                    print("Je hebt de tweede stap van een som nog te vaak volledig fout, oefen deze vaker of vraag je leraar om tips")
                if stapevolledigpergeheel > 0.08:
                    print("Je hebt het eindantwoord van een som nog te vaak volledig fout, oefen deze vaker of vraag je leraar om tips")

                overgpergeheel = float(stapovergeslagen) / float(sommengemaakt)
                if overgpergeheel > 0.15:
                    print("Je slaat te vaak stappen over, op je toets kost dit je mogelijk punten, probeer rustiger sommen uit te werken")
        elif userinput == ("stop"):
            print "Je hebt het programma gestopt"
            print "Bedankt dat je vandaag met ons hebt geoefend"
            print "Mijn scheppers wensen u nog een fijne dag toe :D"
            finished = 10
        else:
            print "Je huidige input wordt niet herkend, gebruik 'cmds' voor hulp"
    elif sommenaanhetmaken == 2:
        print "Wil je nog meer/verder oefenen?"
        print "typ Y in als je verder wilt gaan, typ N in als je wilt stoppen"
        userinput = input("\nVerdergaan: ")
        search = userinput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
        if search != -1:
            userinput = userinput.replace(' ','')
        if userinput == "Y" or userinput == "y":
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
        elif userinput == "N" or userinput == "n":
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
                    print("Goedzo, je antwoord is correct")
                    goed1tussenstap = goed1tussenstap + 1
                    sommenaanhetmaken = 2
                else:
                    if incorrectheden < 5:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout1tussenstap = fout1tussenstap + 1
                        foutinantwoord = foutinantwoord + 1
                    else:
                        print("Nogsteeds incorrect, het juiste antwoord was: " + str(eindantwoord) + " raadpleeg je leraar voor advies")
                        incorrectheden = 0 #reset
                        sommenaanhetmaken = 2
                        foutinantwoord = foutinantwoord + 1
                        fout1tussenstap = fout1tussenstap + 1
                        foutvolledigantwoord = foutvolledigantwoord + 1    
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
                    print("Je hebt het eindantwoord gegeven, dit is correct, maar probeer in de toekomst eerst de tussenstappen te geven")
                    goed1tussenstap = goed1tussenstap + 1
                    stappenovergeslagen = stappenovergeslagen + 1
                    sommenaanhetmaken = 2
                else:
                    if incorrectheden < 2:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout1tussenstap = fout1tussenstap + 1
                        foutinstap1 = foutinstap1 + 1
                    else:
                        print("Nogsteeds incorrect, de juiste stap was: " + str(tussenantwoord1) + " probeer het eindantwoord te geven")
                        incorrectheden = 0 #reset
                        finished = 1
                        fout1tussenstap = fout1tussenstap + 1
                        foutinstap1 = foutinstap1 + 1
                        foutvolledigstap1 = foutvolledigstap1 + 1
            elif finished == 1: #het eindantwoord moet nu gegeven worden
                #deel 1: preparatie van de eerste input
                deelantwoordeninput = input("\nAntwoord: ")
                search = deelantwoordeninput.find(" ") #we kunnen spaties alleen vervangen als ze er zijn, dit moeten we dus eerst checken
                if search != -1:
                    deelantwoordeninput = deelantwoordeninput.replace(' ','')

                #deel 2: controle van de input
                if deelantwoordeninput == eindantwoord:
                    print("Goedzo, je antwoord is correct")
                    goed1tussenstap = goed1tussenstap + 1
                    sommenaanhetmaken = 2
                else:
                    if incorrectheden < 5:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout1tussenstap = fout1tussenstap + 1
                        foutinantwoord = foutinantwoord + 1
                    else:
                        print("Nogsteeds incorrect, het juiste antwoord was: " + str(eindantwoord) + " raadpleeg je leraar voor advies")
                        incorrectheden = 0 #reset
                        sommenaanhetmaken = 2
                        foutinantwoord = foutinantwoord + 1
                        fout1tussenstap = fout1tussenstap + 1
                        foutvolledigantwoord = foutvolledigantwoord + 1
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
                    print("Je hebt het eindantwoord gegeven, dit is correct, maar probeer in de toekomst eerst de tussenstappen te geven")
                    sommenaanhetmaken = 2
                    goed2tussenstap = goed2tussenstap + 1
                    stappenovergeslagen = stappenovergeslagen + 1
                else:
                    if incorrectheden < 2:
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
                    if incorrectheden < 2:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout2tussenstap = fout2tussenstap + 1
                        foutinstap2 = foutinstap2 + 1
                    else:
                        print("Nogsteeds incorrect, de juiste stap was: " + str(tussenantwoord2) + " probeer het eindantwoord te geven")
                        incorrectheden = 0 #reset
                        finished = 2
                        fout2tussenstap = fout2tussenstap + 1
                        foutinstap2 = foutinstap2 + 1
                        foutvolledigstap2 = foutvolledigstap1 + 2
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
                    if incorrectheden < 5:
                        print("Incorrect, probeer het opnieuw.")
                        incorrectheden = incorrectheden + 1
                        fout2tussenstap = fout2tussenstap + 1
                        foutinantwoord = foutinantwoord + 1
                    else:
                        print("Nogsteeds incorrect, het juiste antwoord was " + str(eindantwoord))
                        incorrectheden = 0 #reset
                        sommenaanhetmaken = 2
                        fout2tussenstap = fout2tussenstap + 1
                        foutinantwoord = foutinantwoord + 1
                        foutvolledigantwoord = foutvolledigantwoord + 1
#aanpassing van josso eind (loop)   
