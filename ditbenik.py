#naam van de individu die de programma opent

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

if answer == "16":
    print("                                                               ")
    print("helemaal goed")

if answer == "17":
    print("                                                               ")
    print("Fout! ben niet zo oud")

#Vraag 3

else:
   print("                                                             ")
   print("-------------------------------------------------------------")
   print("Wat is mijn nationalitiet?")
   print("Kies Turks, Arabisch of Russisch")

answer = input()

#Antwoorden Vraag 3

if answer == "Turks": 
    print("                                                               ")
    print("Fout! Veel mensen zeggen dat ik turks lijk maar ik ben niet turks")

if answer == "Arabisch": 
    print("                                                               ")
    print("Fout!")

if answer == "Russisch":
    print("                                                               ")
    print("Goed! хорошо! ik ben russisch")

#Einde van Script

print("                                                                 ")
print("-----------------------------------------------------------------")
print("nou dat was het denk ik, doei!")



       
