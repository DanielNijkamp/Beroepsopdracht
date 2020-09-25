#naam van de individu die de programma opent

import os

print("Hello You, ik ben Daniel")
print("wie ben jij?")

#begroeting en uitleg over Daniel

x = input()
print('Hello, ' + x)
print("                                                                 ")
print("-----------------------------------------------------------------")
print("ik ben een nieuwkomer op het Mediacollege Amsterdam")
print("ik heb een paar vragen gemaakt waardoor je mij beter leert kennen")
print("-----------------------------------------------------------------")
print("                                                                 ")
print("                                                                 ")

#Vraag 1

print("Voordat ik ICT ging leren had ik als vorige opleiding:")
print("       A. Wiskunde en economie")
print("       B. Maatschappijkunde en biologie")
print("       C. Techniek en schijkunde")
print("Kies A, B of C >>>>>>")

answer = input()
    

#Antwoorden Vraag 1

if answer == "A":
    print("Fout! Ik had in de eerste en tweede jaar wel wiskunde maar daarna")
    print("had ik biologie en maatshappijkunde gekozen.")

if answer == "B":
    print("Goed! Ik had in de derde maatschappijkunde en biologie")
    print("als opleiding. heel leuk maar heel complex")

if answer == "C":
    print("Fout! Techniek en schijkunde hadden wij niet op onze school.")
    print("enigste opleidingen die wij hadden waren Wiskunde en Biologie")


#Vraag 2

else:
    print("                                                               ")
    print("---------------------------------------------------------------")
    print("Hoe oud ben ik?(hoe oud ik ben in 2020)")
    print(" Kies 15, 16 of 17")

answer = input()

#Antwoorden Vraag 2


if answer == "15":
    print("                                                               ")
    print("Fout! ben iets ouder.")

elif answer == "16":
    print("                                                               ")
    print("helemaal goed")

elif answer == "17":
    print("                                                               ")
    print("Fout! ben niet zo oud")

#Vraag 3

else:  
    print("                                                             ")
    print("-------------------------------------------------------------")
    print("Wat is mijn nationalitiet?                                   ")
    print("Kies Turks, Arabisch of Russisch                             ")


#Antwoorden Vraag 3

answer = input()
if answer == "Turks":
    print("                                                               ")
    print("Fout! Veel mensen zeggen dat ik turks lijk maar ik ben niet turks")

elif answer == "Arabisch": 
    print("                                                               ")
    print("Fout!")

elif answer == "Russisch":
    print("                                                               ")
    print("Goed! хорошо! ik ben russisch")

else:
    print("                                                                  ")
    print("------------------------------------------------------------------")
    print("Ok dan nu nog een vraag. Welke opleiding heb ik gekozen op het MA?")
    print("                                                                  ")


#Vraag 4 Flowchart

print("                                                                  ")
print("------------------------------------------------------------------")
print("Ok dan nu nog een vraag. Welke opleiding heb ik gekozen op het MA?")
print("Kies uit Software of Game development  [TYPE [software] OF [game] ")


anwser1 = input()
if anwser1 == software:
     print("                                                                  ")
     print("-----------------------------------------------------------------")
     print("Ok dus wat voor developer ben ik? Front-end of back-end?         ")
     print("TYPE [front] OF [back]                                           ")


     answer2 = input()
elif anwser2 == front:
    print("Fout!, ik ben front end Gamedeveloper")

elif answer2 == back:
    print("Fout!, ik ben front end Gamedeveloper")


if anwser1 == Game:
     print("                                                                  ")
     print("-----------------------------------------------------------------")
     print("Ok dus wat voor developer ben ik? Front-end of back-end?         ")
     print("TYPE [front] OF [back]                                           ")

     anwser3 = input()

elif anwser3 == front:
     print("Goed!, ik ben front end Gamedeveloper")



elif anwser3 == back:
     print("Fout!, ik ben front end Gamedeveloper")
   

else:
     print("                                                                  ")
     print("-----------------------------------------------------------------")
     print("Nou dat was het, doei!                                           ")
    





















