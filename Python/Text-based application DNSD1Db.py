#import stuff
import random, keyboard, os

#als een einde is behaald dan veranderd de waarde en eindigd de programma
appEnding = 1

#generate number 1 through 4 to simulate a 1 in 4 change.
davielifeStatus = random.randint(1,4)

#als davie dood is dan is de status "dead"
if davielifeStatus == 1:
    davielifeStatus = "dead"

#als davie leeft dan is de status "alive"
if davielifeStatus == 2 or davielifeStatus == 3 or davielifeStatus == 4:
    davielifeStatus = "alive"



#generate number 1 through 2 to simulate a 50% change
aantalAA = random.randint(1,2)

#if aantalAA = 1 dan kom je grote groep vluchtelingen tegen
if aantalAA == 1 :
    aantalAB = "grote"

#if aantalAA = 2 dan kom je kleine groep vluchtelingen tegen
if aantalAA == 2:
    aantalAB = "kleine"
        

#Als er in slovakije leden blijven en je gaat naar de westen gaat reizen
groepblijftinSlovakije = random.randint(1,2)


#kans dat jullie verdrinken midden op zee
boatStatus = random.randint(1,5)

#als boatStatus 1 is dan zinkt de boot
if boatStatus == 1:
    boatStatus = "Sinking"

#als boatStatus 2, 3, 4 of 5 is dan zinkt de boot niet
if boatStatus == 2 or boatStatus == 3 or boatStatus == 4 or boatStatus == 5:
    boatStatus = "notSinking"


#kans dat jullie worden aangehouden door politie
policeStatus = random.randint(1,5)

#als policeStatus 1 is dan worden jullie opgepakt
if policeStatus == 1:
    policeStatus = "opgepakt"

#als policeStatus 2, 3, 4 of 5 is worden jullie niet opgepakt
if policeStatus == 2 or policeStatus == 3 or policeStatus == 4 or policeStatus == 5:
    policeStatus = "nietopgepakt"


#kans dat er leden dood gaan
groupDeaths = random.randint(1,3)

if groupDeaths == 1:
    groupDeaths = "Y"

if groupDeaths == 2 or groupDeaths == 3:
    groupDeaths = "N"



def space1():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("                                                                                                        ") 
    print("                                                                                                        ")
    print("                                                                                                        ") 
    print("                                                                                                        ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def space2():
    print("                                                                                                        ")
    print("                                                                                                        ")

#Start menu
introRunning= True
backtoMenu = 1


#Intro message 
print("================================================")
print("Hallo en welkom bij de text-based adventure van Daniel Nijkamp SD1Db")
print("Klik E om te beginnen")
print("Klik Q om af te sluiten")
print("Klik I voor contact en auteur")
print("================================================")

#exit hotkey
while introRunning == True:
    if keyboard.is_pressed('i'):
        space1()
        print("Auteur/Maker : Daniel Nijkamp")
        print("Studentnummer : 31644")
        print("school e-mail: 31644@ma-web.nl")
        print("persoonlijke e-mail: danielnijkamp2004@gmail.com")
        print("als je vragen hebt, vraag me!")
        print("klik U om terug te gaan")
        backtoMenu = 2
        keyboard.wait('u')  

    #back to intro message
    if backtoMenu == 2 and keyboard.is_pressed('u'):
        space1()
        print("================================================")
        print("Hallo en welkom bij de text-based adventure van Daniel Nijkamp SD1Db")
        print("Klik E om te beginnen")
        print("Klik Q om af te sluiten")
        print("Klik I voor contact en auteur")
        print("================================================")
        backtoMenu = 1

    if keyboard.is_pressed('=') and keyboard.is_pressed('-'):
        print("STATUS")
        print("DavielifeStatus = " + davielifeStatus)
        print("aantalAA =" + str(aantalAA))
        print("slovakije groep = "+ str(groepblijftinSlovakije))
        print("boatStatus = "+ boatStatus)
        print("policeStatus =" +policeStatus)
        print("GroupDeaths = "+groupDeas)
        introRunning = False
        break

    #exit program
    if keyboard.is_pressed('q'):
        exit()

    #end menu and start app
    if keyboard.is_pressed('e') and backtoMenu == 1:
        introRunning = False
        break

#start of app
#DEEL 1
#VRAAG 1
space1()
print("DEEL 1")
space2()
print("Jij bent Maksur Mahzuz je woont in de stad genaamd Aleppo en je staat slaperig op en je loopt naar de woonkamer.")
print("terwijl je je ochtend routine begint Davie met Jadid in hand de ochtendjournaal te kijken.")
print("jij en Davie hebben een gesprek over de protest buiten hun huis.")
print("Op dat moment zien jullie een live-uitzending van protesten in andere steden zoals Damascus en ook hun stad Aleppo.")
space2()
print("jij krijgt hier de keuze om de beelden op tv verder te kijken naar de beelden in Damascus en de centrum van Aleppo, of je kan uit je raam kijken naar de protesten in jouw straat. ")
print("kies uit [kijk naar de beelden op je tv] of [kijk uit je raam]")

#input vraag 1
inputA = input()

#antwoord 1.1
if inputA == "kijk naar de beelden op je tv":
    space1()
    print( "je ziet op de tv de beelden van Aleppo en Damascus")
    print("Terwijl de journalisten op de locatie de situatie proberen uit te leggen wordt er geschoten.")
    print("de situatie escaleert en je hoort opeens schoten buiten je huis")
    print("Terwijl de signaal van de journalist word gestopt, hoor je na een paar minuten explosies buiten je huis. ")
    space1()

#antwoord 1.2
if inputA == "kijk uit je raam":
    space1()
    print("je kijkt buiten je raam en ziet een grote groep mensen die vlaggen en borden hijsen." )
    print("daarna hoor je schoten en zie je mensen weg rennen.")
    print("Na een paar minuten hoor je ook explosies buiten je huis.")
    space1()

#klik enter om door te gaan
input("Typ [Enter] om door te gaan")

space1()
print("DEEL 2")
#Kans dat Davie dood gaat | 1 op de 4 | als davie dood is dan komt deze dialoog
if davielifeStatus == 1:
    space1()
    print("er explodeert een bom naast jouw huis en je huis stort in. je vrouw Davie gaat dood maar jij en je zoon Jadid leven nog")
    print("jij staat op en je zoekt door de puinhoop en je vind Jadid en jullie vluchten")
    space1()


space1()
#Als Davie dood is komt deze dialoog daarna
print("Terwijl er meer en meer chaos ontstaat in de stad hoor jij meer en meer kogelschoten en knallen is de buurt van jouw huis.")
if davielifeStatus == 1:
    print("je kan nu aleen vluchten, typ [vluchten]")

#als Davie dood is komt deze dialoog daarna
if davielifeStatus == "alive":
    print("Jij hebt de keuze om hier te blijven in je huis of met je familie te vluchten.")
    print("kies uit [in je huis blijven] of [vluchten] ")

#input vraag 2
inputB = input()

#antwoord 2.1
#Als Davie nog leeft en je typt: "in je huis leven" komt deze dialoog daarna
if inputB == "in je huis blijven" and davielifeStatus == "alive":
    space1()
    print("je hebt gekozen om in je huis te blijven en de deur van zijn appartement te barricaderen.")
    print("jullie blijven daar voor een paar minuten totdat er een bom ontploft in de buurt van jouw huis.")
    print("Jouw huis stort in en je vrouw Davie gaat dood")
    space2()
    print("Jij vlucht samen met Jadid uit de puinhoop en vinden een "+ aantalAB+ " groep vluchtelingen.")
    print("Met de groep vinden jullie een man genaamd Zaeim Jarufah die zegt dat hij mensen kan helpen met vluchten uit Syrië.")
    print("Na de dood van Maksur’s vrouw besluit Maksur met hun mee te gaan.")
    space1()
#antwoord 2.2  
#als Davie dood is en je typt "in je huis blijven" dan komt deze dialoog daarna
if inputB == "in je huis blijven" and davielifeStatus == "dead":
    space1()
    print("jouw huis is ingestort dus jij besluit om te vluchten")
    print("jullie vluchten uit het gebouw en vinden een "+ aantalAB + " groep vluchtelingen.")
    print("Met de groep vluchtelingen vinden jullie een man genaamd Zaeim Jafurah die mensen kan helpen met het vluchten naar Turkije en verder.")
    print("Jullie besluiten met Zaeim Jafurah mee te gaan") 
    print("Minuten nadat jij en je familie zijn gevlucht uit hun huis ontploft er een bom naast hun huis. Daarna stort het hele gebouw in achter hun terwijl ze vluchten")
    space1()

#als Davie nog leeft en je typt "vluchten" dan komt deze dialoog daarna
if inputB== "vluchten" and davielifeStatus == "alive":
    space1()
    print("jullie hebben besloten om te vluchten, jullie vluchten uit het gebouw en vinden een "+ aantalAB + " groep vluchtelingen.")
    print("Met de groep vluchtelingen vinden jullie een man genaamd Zaeim Jafurah die mensen kan helpen met het vluchten naar Turkije en verder.")
    print("Jullie besluiten met Zaeim Jafurah mee te gaan") 
    print("Minuten nadat jij en je familie zijn gevlucht uit hun huis ontploft er een bom naast hun huis. Daarna stort het hele gebouw in achter hun terwijl ze vluchten")
    space1()

#als je huis is ingestort door de explosie dan kan je aleen vluchten, als dat zo is dan komt deze dialoog daarna   
if inputB == "vluchten" and davielifeStatus == "dead":
    space1()
    print("jullie hebben besloten om te vluchten, jullie vluchten uit het gebouw en vinden een "+ aantalAB + " groep vluchtelingen.")
    print("Met de groep vluchtelingen vinden jullie een man genaamd Zaeim Jafurah die mensen kan helpen met het vluchten naar Turkije en verder.")
    print("Jullie besluiten met Zaeim Jafurah mee te gaan") 
    print("Minuten nadat jij en je familie zijn gevlucht uit hun huis ontploft er een bom naast hun huis. Daarna stort het hele gebouw in achter hun terwijl ze vluchten")
    space1()


#als je in je huis blijft dan gaat davie dood
if inputB == "in je huis blijven" and davielifeStatus == "alive":
    davielifeStatus = 1

    
#klik enter om door te gaan
input("Typ [Enter] om door te gaan")

#Deel 3
space1()
print("DEEL 3")
space2()
print("de groep volgen Zaeim naar een kleine transport truck waar de groep achterin gaat zitten terwijl Zaeim voor de stuur gaat.")
print("Terwijl de groep krap naast elkaar staan en zitten proberen ze de donkere kamer te verlichten.") 
print("Een van de leden trekt uit zijn zak een aansteker waarmee hij de kamer een klein beetje verlicht.")
print("Terwijl jullie ver weg van Aleppo rijden horen jullie meer en meer kogelschoten en bommen in de centrale gebied van Aleppo.")
space1()
print("Terwijl de groep praat over wat er gebeurt in Aleppo, overhoor jij een gesprek waarbij je hoort dat er militaire geweld wordt gebruikt in Damascus en dat ze ook bij Aleppo zullen zijn.")
print("Maksur vraagt wat er aan de hand is aan de andere leden die naast hem staan. Een persoon achterin de groep vertelt hun: “er begaat een burgenoorlog tussen rebbellen en de overheid.") 
print("Ik denk niet dat we hier veilig zijn”. Nadat je dit hoort valt je hart en verliest hij hoop dat hij terug kan gaan naar zijn huis.")
print("Je staat daar en je wilt iets vragen aan de groepsleden maar je bent zo gebroken dat je geen woorden hebt voor wat er net is gebeurd.")
print("Hij probeert zichzelf te kalmeren en staat daar en denkt eraan of hij misschien een vraag moet stellen.") 
space2()
#klik enter om door te gaan
input("Typ [Enter] om door te gaan")

space2()
#VRAAG 3
print("je krijgt de opties om iets te vragen aan een van de leden")
print("kies uit [...] of [hoe zit het met de rest van de mensen die daar zitten] of [waar gaan we naartoe]")

#input vraag 1
inputC = input()

#antwoord 3.1
if inputC == "..." or inputC == ".." or inputC == "....." or inputC == "....":
    space1()
    print("je blijft stil na het antwoord dat de man had gegeven. je zet je hand op je voorhoofd en daarna leun je met je rug tegen de muur.")
    print("Daarna ga je  langzaam naar beneden totdat je op de grond zit met je handen op je  knieën en met je hoofd gericht op de vloer.")
    print("De man kijkt jouw aan en hij loopt naar je toe, vervolgens zegt hij: “het komt wel goed, op een of andere manier komen we wel terug.") 
    print("Een andere man reageert: “blijft er dan wel iets staan om ervoor terug te komen?” je blijft daarna stil en je kijkt depressief naar de grond.")

#antwoord 3.2
if inputC == "hoe zit het met de rest van de mensen die daar zitten":
    space1()
    print("Maksur zegt: “hoe zit het met de rest van de mensen die daar zitten? Gaan zij het overleven?”.")
    print("De man antwoord: “zij zijn dood, de gene die niet dood zijn zullen rotten onder de puinhoop van Aleppo")
    print("Zij hebben geen hoop meer, wij moeten nu aan ons denken om van hier weg te gaan.")
    print("Terwijl je denkt aan de mannen, vrouwen en kinderen die nog in Aleppo zitten zet Maksur zijn rug tegen de muur en gaat hij langzaam naar beneden") 
    print("totdat hij op de grond zit met zijn handen op zijn knieën en met zijn hoofd gericht naar de vloer.")

#antwoord 3.3
if inputC == "waar gaan we naartoe":
    space1()
    print("Je vraagt aan de groep of ze weten waar ze naartoe gaan. Een van de leden komt naar voren en zegt: “weg van hier zover ik weet, Zaeim zei dat we via Turkije en de Kaukasus naar Europa zullen gaan.")
    print("Hopelijk komen we daar aan zonder problemen”. Terwijl Maksur denkt aan de mannen, vrouwen en kinderen die nog in Aleppo zitten zet hij zijn rug tegen de muur")
    print("en gaat hij langzaam naar beneden totdat hij op de grond zit met zijn handen op zijn knieën en met zijn hoofd gericht naar de koude vloer.")
    print("Je denk aan hoe jullie naar Europa gaan en hoe meer Maksur erover na denk hoe meer het lijkt dat het onmogelijk is.")

#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")

space1()
#DEEL 4
print("Deel 4")
space1()

#als davie leeft komt deze dialoog
if davielifeStatus == "alive":
    print("Nu zit Maksur op de grond met zijn handen op zijn hoofd na te denken over alles waar hij over kan nadenken")
    print("zijn vrouw Davie en zijn zoon Jadid komen naast hem zitten en proberen hem te gemoed te stellen.")
    print("je laat je handen zakken zodat je handen naast je zit.")
    print("Davie en Jadid zetten hun hand op jouw hand en ze zeggen ondersteunende woorden als: “het komt goed”.")

#klik enter om door te gaan
    input("Typ [Enter] om door te gaan")

    space2()
    print("na de gesprekken zegt Zaeim: “het gaat nog lang duren totdat we bij de grens zijn dus neem wat rust”.")
    print("Iedereen begint te slapen en gebruiken hun kleding als dekens en kussens.")
    print("Jadid en Davie liggen naast jouw en je besluit je jas uit te doen en het op Jadid te leggen als een deken.")
    print("jullie zitten allemaal naast elkaar met jullie hoofden tegen elkaar en een voor een vallen jullie in slaap")

#klik enter om door te gaan
    space2()
    input("Typ [Enter] om door te gaan")

#als davie dood is komt deze dialoog
if davielifeStatus == 1:
    print("Nu zit Maksur op de grond met zijn handen op zijn hoofd na te denken over alles waar hij over kan nadenken.")
    print("Zijn liefde van het leven Davie is dood en hij kan er niks aan doen.")
    print("Hoe moet hij dit nu aan Jadid vertellen? Hoe moet hij verder leven terwijl hij weet dat zijn moeder dood is gegaan?")
    print("Hoe gaat hij ermee om als hij hoort dat zijn moeder dood is?")
    print("precies wanneer Maksur zit te denken komt Jadid en zet zijn hand op Maksur’s arm en zegt: “papa waar is mama?”")
    space2()

#als davie dood is komt ook deze vraag
    print("jij hebt hier de keuze om iets te zeggen")
    print("kies uit [...]  of [ ik weet niet]")

#input vraag 4
    inputD = input()

    #antwoord 4.1
    if inputD == "..." or inputD == "..." or inputD == "...." or inputD == ".....":
        space1()
        print("je hebt gekozen om stil te blijven en geen antwoord te geven aan Jadid. Jadid vraagt daarna nog een keer: “papa waar is mama?”")
        print("nogmaals blijf je  stil en je hebt de moed niet om te zeggen dat zijn moeder dood is. Jadid begint te huilen en vraag voor de derde keer: “papa waar is mama?!” in een iets hardere maar droevige stem")
        print("je kijkt hem in de ogen en je blijft stil, daarna kijk je weer naar de grond, je begint daarna ook te huilen, maar terwijl je tranen lans je wangen gaan voelt je alleen leeghieid. zijn gedachtes zijn stil en hij zet zijn armen levenloos naast zich.")
        print("Jadid begint naast je in een opgekropen manier te liggen met zijn hoofd op je arm.")
        print("je voelt de tranen van Jadid op je arm en blijft stil")
        space2()
        print("na de gesprekken zegt Zaeim: “het gaat nog lang duren totdat we bij de grens zijn dus neem wat rust.”") 
        print("Iedereen begint te slapen en gebruiken hun kleding als dekens en kussens.")
        print("Jadid ligt naast je en je besluit je jas uit te doen en het op Jadid te leggen als een deken.")
        print("je doet zijn arm over Jadid en begint ook te slapen.")

    #antwoord 4.2
    if inputD == "ik weet het niet" or inputD == "ik weet niet":
        space1()
        print("je zegt tegen Jadid dat hij niet weet waar Davie is, je valt op de grond en je zet je handen op je hoofd.")
        print("je begint te huilen en je weet niet wat je verder moet zeggen. je voelt je slecht dat je tegen je eigen zoon liegt maar je weet niet of jij iets anders kan zeggen")
        print("je  zegt weer in een stille stem dat je het niet weet. je zit op de grond te huilen met je handen op je hoofd en je knieën dichtbij je borst.")
        print("Jadid begint ook te huilen en zit naast je. jullie zitten nu naast elkaar te huilen en blijven stil.")
        space2()
        print("na de gesprekken zegt Zaeim: “het gaat nog lang duren totdat we bij de grens zijn dus neem wat rust.”") 
        print("Iedereen begint te slapen en gebruiken hun kleding als dekens en kussens.")
        print("Jadid ligt naast je en je besluit je jas uit te doen en het op Jadid te leggen als een deken.")
        print("je doet zijn arm over Jadid en begint ook te slapen.")

space1()
print("10 uur later...")

#klik enter om door te gaan
input("Typ [Enter] om door te gaan")

#deel 5
space1()
print("Deel 5")
space2()
print("jullie zijn door een droge woestijn gereden voor een lange tijd, jij wordt langzaam wakker en je hoort dat de truck stopt.")
print("je ziet nog dat iedereen slaapt maar jij gaat alvast naar buiten")
print("Jij gaat naar buiten en ziet Zaeim roken terwijl hij op de autokap leunt. je loopt naar hem toe en je ziet een klein dorpje voor je")
print("naast het dorp zie je ook een grote rivier met mensen die hun kleding wassen en kinderen die zitten te zwemmen")
print("je vraagt aan Zaeim waar ze zijn, hij zegt: “We zijn in jarãbulus, nog een paar kilometers hier vandaan is de grens van Turkije“")
print("“nadat we de grens over zijn kunnen we langs de rivier rijden of we kunnen via een snelweg rijden naar de grens.“")

space2()
#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")


#vraag 5
space2()
print("Je krijgt hier de keuze om te kiezen of jij en de groep via de rivier gaan of via de snelweg gaan.")
print("kies uit [langs de rivier] of [via de snelweg]")

#input vraag 5
inputE = input()

#antwoord 5.1
if inputE == "langs de rivier" or inputE == "via de rivier":
    space1()
    print("je zegt tegen Zaeim dat het beter is als we via de rivier rijden.")
    print("Hij zegt: “Goed idee alleen als we gepakt worden dan was alles voor niks.")
    print("je kijkt naar het dorpje verderop en zegt: “hoe zit het met dat dorpje daar?”")
    print("Zaeim gooit zijn sigaret op de grond en steekt een nieuwe aan, dan zegt hij: “we hebben geen gas meer voor onze truck dus ik moet even zoeken of zij nog wat hebben.")
    print("jullie kunnen ondertussen daar even wat eten en drinken halen en wat rust nemen. Hopelijk kunnen we morgen weg.”")
    space1()

#antwoord 5.2
if inputE == "via de snelweg" or inputE == "langs de snelweg":
    space1()
    print("je zegt tegen Zaeim dat het beter is als we via de snelweg rijden")
    print("Zaeim zegt: “Ja goed idee alleen als de bij de grens gepakt worden of onderweg worden opgepakt dan zijn we de lul”.")
    print("je ziet voor je een dorp en je en zegt: “hoe zit het met dat dorpje daar?”")
    print("Zaiem gooit zijn sigaret op de grond en steekt een nieuwe aan")
    print("dan zegt hij: “we hebben geen benzine meer voor de truck dus ik ga met wat handelaren onderhandelen of ik een jerrycan kan regelen voor de truck")
    print("en jullie kunnen daar even wat eten en drinken halen, wat rust nemen of nog iets anders wat jullie nodig moeten. Hopelijk kunnen we morgen weg”.")
    space1()

#klik enter om door te gaan
input("Typ [Enter] om door te gaan")


#als davie dood is komt deze dialoog daarna
if davielifeStatus == 1:
    space1()
    print("Zaeim geeft jouw 7.000 pond en zegt: “hier koop wat eten en kleding voor je zoon”.")
    print("je gaat terug naar de truck toe en je maakt Jadid wakker")
    print("je vraagt of hij honger heeft en Jadid schud ja met zijn hoofd")
    print("Je zegt: “kom we gaan wat eten halen”. jullie lopen hand in hand met het dorp in zicht.")
    print("Terwijl jullie naar het dorp lopen komt de zon naar boven.")

    space2()
#klik enter om door te gaan
    input("Typ [Enter] om door te gaan")

    space2()
    print("Terwijl jullie naar het dorpje lopen zien jullie een super drukke markt met kraampjes")
    print("kraampjes die verschillende dingen verkopen zoals eten, kleding, kledingstof en zelf gemaakte sieraden.")
    print("Na 5 minuten lopen komt er een man naar jullie toe en groet jullie en zegt: “welkom in Jarãbulus“") 
    print("koop gerust onze voedsel en spullen!”. Jullie lopen langs de markt en ziet een eet kraampje.")

    space2()
#klik enter om door te gaan
    input("Typ [Enter] om door te gaan")

    space2()
    print("Jij en Jadid lopen naar een kebab kraampje en Maksur zegt: “twee kebab graag”.")
    print("De man zegt: “3000 pond graag” en je geeft hem de geld.")
    print("Jullie wachten voor een paar minuten en jullie krijgen daarna 2 kebab gerechten")
    print("jij geeft één aan Jadid en jullie beginnen te eten, daarna kijken jullie voor wat kleding en vinden een kleding kraampje")
    print("jij koopt een dik jasje voor Jadid en de man zegt: “4000 pond alstublieft” je geeft hem het geld en jullie lopen verder.")
    print("jullie vinden daarna een man die jullie een slaap plek aanbieden, jullie vinden het een goed idee en de man leid jullie naar de slaap plek.")
    print("Jullie komen een kamer binnen met een olielamp op een klein kast. er zijn 3 grote bergen van hooi en textiel die op een bed horen te lijken.")
    print("Jullie besluiten hier te slapen voor de nacht, nadat jullie elkaar tegen elkaar slaaplekker zeggen vallen jullie in slaap.")
    


#als davie leeft komt deze dialoog daarna
if davielifeStatus == "alive":
    space1()
    print("Zaeim geeft jouw 8.000 pond en zegt: “hier koop wat eten en kleding voor je zoon en vrouw”")
    print("je gaat terug naar de truck toe een maakt Jadid en Davie wakker")
    print("je vraagt of ze honger hebben en Jadid schud ja met zijn hoofd.")
    print("Davie zegt dat het een goed idee is als ze wat te eten kunnen krijgen")
    print("ze stappen uit de truck en lopen met elkaar hand in hand dorp in zicht.")
    print("Terwijl ze lopen zien ze de zon opgaan voorbij de horizon achter het dorp.")
          
    space1()
#klik enter om door te gaan
    input("Typ [Enter] om door te gaan")

    space1()
    print("Terwijl jullie naar het dorpje lopen zien jullie een super drukke markt met kraampjes")
    print("kraampjes die verschillende dingen verkopen zoals eten, kleding, kledingstof en zelf gemaakte sieraden.")
    print("Na 5 minuten lopen komt er een man naar jullie toe en groet jullie en zegt: “welkom in Jarãbulus“") 
    print("koop gerust onze voedsel en spullen!”. Jullie lopen langs de markt en ziet een eet kraampje.")

    space1()
#klik enter om door te gaan
    input("Typ [Enter] om door te gaan")

    space1()
    print("Jullie lopen naar een kebab kraampje en je zegt: “drie kebab graag”. De man zegt: “4500 pond graag” en je geeft hem de geld.")
    print("Na een paar minuten krijgen jullie 3 kebab gerechten en beginnen jullie te eten, daarna kijken jullie nog verder voor wat kleding, jullie vinden een kleding kraampje waar jullie een jas vinden voor Jadid.")
    print("Jullie kiezen een dikke jas en de man achter de kraampje zegt: “3500 pond alstublieft”. Jij geeft hem de geld en je geeft daarna de jas aan Jadid, daarna lopen jullie verder en vinden jullie een man die jullie een slaap plek aanbied.")
    print("Jullie vinden het een goed idee en lopen met de man mee, hij leid jullie naar een donkere kamer die wordt verlicht door een olielamp op een kleine kasje. Op de grond zijn er 3 grote bergen hooi en textiel die op een bed horen te lijken.")
    print("Jullie besluiten hier te blijven voor de nacht en nadat jullie elkaar een goede nachtrust wensen vallen jullie in slaap.")

space1()
print("9 uur later...")

#klik enter om door te gaan
input("Typ [Enter] om door te gaan")

#deel 6
space1()
print("Deel 6")
space1()

print("je wordt wakker en je hoort Zaeim praten met 2 andere mensen")
print("hij heeft een jerrycan van benzine in zijn handen. Zaeim loopt daarna naar de truck toe en jij staat op en vraagt het wat er is gebeurt.")
print("Zaeim zegt: “niks maar we hebben gas voor de truck dus we kunnen gewoon weer gaan”")

#als davie dood is komt deze dialoog daarna
if davielifeStatus == "dead":
    print("Zaeim zegt: “maak je zoon wakker we gaan zo weg”")

    space2()
    print("Maksur maakt Jadid wakker en zegt dat ze weer moeten gaan.")
    print("jullie lopen naar de truck toe en jullie zien Zaeim de truck bijtanken.")
    print("Jullie gaan weer in de achterkant van de truck zitten met de rest van de groep.")
    print("Je hoort de truck opstarten en de truck begint te rijden")

#als davie leeft komt deze dialoog daarna
if davielifeStatus == "alive":
    print("Zaiem zegt: “maak je zoon en vrouw wakker we gaan zo weg”")

    space2()
    print("Je maakt Jadid en Davie wakker en zegt dat ze weer moeten gaan.")
    print("jullie lopen naar de truck toe en jullie zien Zaeim de truck bijtanken.")
    print("Jullie gaan weer in de achterkant van de truck zitten met de rest van de groep.")
    print("Je hoort de truck opstarten en de truck begint te rijden")

#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")

space1()
print("1 uur later")
space2()
#jullie komen bij de grens van Syrie en Turkije
print("Jullie komen aan bij de grens en iemand in de groep zegt: “iedereen blijf stil!”.")
print("Je overhoort een gesprek met Zaeim en de douane. Ze bespreken de documenten.")
print("Na een paar minuten hoor je Zaeim weer naar binnen stappen en de motor opstarten.")

#als je hebt gekozen om via de snelweg te rijden dan komt deze dialoog daarna
if inputE == "via de snelweg" or inputE == "langs de snelweg":
    print("julle rijden langs de grens zonder problemen en rijden dan langs een smalle weg")
    print("daarna beginnen jullie te rijden op een weg en dan via een snelweg")
    

#als je hebt gekozen om langs de rivier te rijden dan komt deze dialoog daarna
if inputE == "langs de rivier" or inputE == "via de rivier":
    print("daarna rijden julle voorbij de grens en langs de rivier")

    print("Jullie rijden op de weg totdat jullie uit de zicht zijn van de douane daarna rijden jullie langs de rivier")
    print("de truck wiebelt heen en weer. jullie rijden voor een paar uur langs de rivier zonder dat iemand jullie heeft gezien") 
    print("daarna komen jullie aan bij een groot meer en gaan jullie op de snelweg. ")


#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")
     
#er is een kans dat jullie [ONDERWEG] worden aangehouden door de politie, als dit gebeurt dan komt deze dialoog daarna.
if policeStatus == "opgepakt":
    space1()
    print("9 uur later")
    space2()
    print("jullie worden onderweg gestopt en je hoort Zaeim te praten met een paar politie agenten")
    print("er wordt gevraagd of de truck geopend kan worden.")
    print("Jullie worden aangehouden door de politie en worden naar de politie bureau gestuurd.")
    print("Daar worden jullie in de gevangenis gestuurd totdat er bewijs is dat jullie onschuldig zijn.")
    print("Jullie zitten een paar weken in de gevangenis en de gevangen worden heel streng behandeld.")
    
    #kans dat er een paar leden dood gaan wegens de omstandigheden, als dat gebeurt dan komt deze dialoog
    if groupDeaths == "Y":
        space2()
        print("Jij wordt later vrij gelaten met een paar andere leden maar de groep is veel kleiner dan het eerst was.")
        print("Je hebt nog niet gehoord van ze en je weet niet waar de rest zijn.")
        print("Maar jullie worden daarna vrijgelaten en gaan verder met de reis.")
        policeStatus = "nietopgepakt"

    #als er niemand in de groep dood gaat wegens omstandigheden dan komt deze dialoog
    if groupDeaths == "N":
        space2()
        print("jullie worden later allemaal vrijgelaten")
        print("gelukkig zijn meeste van jullie in orde, sommige leden hebben paar klachten wegens de omstandigheden")
        print("maar jullie gaan daarna gewoon weer verder met de reis")
        policeStatus = "nietopgepakt"



#als jullie niet [ONDERWEG] worden opgepakt dan komt deze dialoog
space1()
print("14 uur later...")
print("Jullie komen aan bij de grens van Turkije en Georgië.")
print("Jullie stoppen weer en je hoort Zaeim weer overleggen met de douane.")


#er is een kans dat jullie worden aangehouden [BIJ DE GRENS] door de politie, als dit gebeurt dan komt deze dialoog daarna.
if policeStatus == "opgepakt":
    space1()
    print("er wordt gevraagd of de truck geopend kan worden.")
    print("Jullie worden aangehouden door de politie en worden naar de politie bureau gestuurd.")
    print("Daar worden jullie in de gevangenis gestuurd totdat er bewijs is dat jullie onschuldig zijn.")
    print("Jullie zitten een paar weken in de gevangenis en de gevangen worden heel streng behandeld.")

    #kans dat er een paar leden dood gaan wegens de omstandigheden, als dat gebeurt dan komt deze dialoog
    if groupDeaths == "Y":
        space2()
        print("Jij wordt later vrij gelaten met een paar andere leden maar de groep is veel kleiner dan het eerst was.")
        print("Je hebt nog niet gehoord van ze en je weet niet waar de rest zijn.")
        print("Maar jullie worden daarna vrijgelaten en gaan verder met de reis.")

    #als er niemand in de groep dood gaat wegens omstandigheden dan komt deze dialoog
    if groupDeaths == "N":
        space2()
        print("jullie worden later allemaal vrijgelaten")
        print("gelukkig zijn meeste van jullie in orde, sommige leden hebben paar klachten wegens de omstandigheden")
        print("maar jullie gaan daarna gewoon weer verder met de reis")


#als jullie voorbij de grens komen zonder problemen dan komt deze dialoog daarna
space1()
#deel 7
print("Deel 7")
space2()
print("Jullie rijden voorbij de grens van Turkije en rijden op de snelweg en rijden zonder problemen naar Sokhumi.")
print("Een haven in Georgië. Jullie stappen uit de truck en gaan op een klein opblaasboot met een klein motor aan de achterkant,")
print("jullie starten de motor en gaan op reis.")

#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")


#deel 8
space1()
print("Deel 8")
space2()
print("Jullie zitten op zee geen land in zicht, jullie hebben wat water en wat eten mee genomen alleen omdat het zo lang hebben jullie nog weinig over.")
print("er ontstaat een discussie over wat eten, de discussie escaleert en een of twee worden overboord gegooid.")
print("Iedereen wordt in paniek gegooid, terwijl iedereen tegen elkaar schreeuwt proberen een paar mensen de mensen in het water eruit te halen.")

space2()
#vraag 6
print("jij hebt hier de keuze om iets te zeggen")
print("kies uit [iedereen blijf kalm] of [stop met vechten]")

#input vraag 6
inputF = input()

#antwoord 6.1
if inputF == "iedereen blijf kalm" or inputF == "blijf kalm":
    space1()
    print("Je schreeuw: “iedereen blijft kalm” maar de gene die boos zijn luisteren")
    print("sommige kijken je wel aan en hebben het gehoord maar negeren je")

#antwoord 6.2
if inputF == "stop met vechten" or inputF == "stop":
    space1()
    print("Je schreeuwt: “stop met vechten”.")
    print("Ze stoppen voor een paar seconden maar ze gaan daarna weer verder.")

print("je ziet een paar mensen verdrinken")

#kans dat er perongeluk een gat wordt gemaakt in de boot waardoor de boot zinkt en jullie verdrinken | EINDE 1
if boatStatus == "Sinking":
    space2()
    print("door de paniek wordt er perongeluk een gat gemaakt in de zijkant van de boot")
    print("de boot zinkt en jullie verdrinken [Einde 1]")
    appEnding = 2
    if appEnding == 2:
        input("Typ [Enter] om de programma af te sluiten")
        exit()



print("paar mensen zijn verdronken maar er zijn ook een paar uit de boot geholpen")
print("paar leden waren ervan overtuigd dat de mensen die overboord waren gegooid")
print("slechte en egoïtische mensen waren, ze wouden dat het eten gelijk werd verdeeld")
print("uiteindelijk blijft het super stil omdat er geen eten en drinken meer is")
print("en omdat er niemand comfortabel genoeg is om iets te zeggen")
print("gellukig zijn jullie al bijna in de buurt van Oekraïne")


#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")

#Deel 9
space1()
print("Deel 9")

space2()
print("Jullie komen aan in Krimea bij een grote haven, jullie stappen uit de boot en lopen langs de haven.") 
print("Jullie gaan naar een warenhuis toe met een truck, jullie stappen weer in en rijden Mykoliav.")
print("Een stad niet ver van de Krimea. Daar gaan jullie op een vrachttrein naar Slowakije toe ")

space2()
print("12 uur later....")

#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")

#Deel 10
print("Deel 10")

space2()
print("Jullie komen aan in Bratislava, jullie stappen uit en jullie gaan naar een warenhuis toe.")
print("Je ziet Zaeim praten met een andere man. Zaeim zegt: “ik ga weg jullie gaan verder met deze man“")
print("ik ga terug naar het Midden-Oosten en proberen andere mensen te helpen. De man stelt zich voor als Akram Zaher.")
print("Hij zegt dat het even gaat duren totdat we naar het westen kunnen reizen.")
print("Hij zegt dat we hier kunnen blijven of dat we na 2 maanden naar Duitsland en Nederland kunnen gaan.")

#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")

space2()
#vraag 7
print("je krijgt hier de keuze om te blijven of naar Duitsland en Nederland te gaan")
print("kies uit [ blijf in slovakije] of [naar het westen reizen]")

#input vraag 7
inputG = input()

#vraag 7.1 | einde 2 | als je in slovakije wilt blijven en Davie is dood dan komt deze dialoog
if inputG == "blijf in slovakije" and davielifeStatus == "dead" or inputG == "in slovakije blijven" and davielifeStatus == "dead":
      space1()
      print("Zaeim zegt dat hij een huis voor jullie heeft geregeld.")
      print("Hij rijd jullie naar jullie huis en wanneer jullie uitstappen zegt hij half serieus: “regel jezelf een goeie vrouw he”.")
      print("Jullie leven nog een rustige leven verder. [Einde 2]")
      space2()
      appEnding = 2
      if appEnding == 2:
          input("Typ [Enter] om de programma af te sluiten")
          exit()

#vraag 7.2 | einde 2 | als je in slovakije wilt blijven en Davie leeft nog dan komt deze dialoog
if inputG == "blijf in slovakije" and davielifeStatus == "alive" or inputG == "in slovakije blijven" and davielifeStatus == "alive":
      space1()
      print("Zaeim heeft een huis geregeld voor Maksur, Davie en Jadid.")
      print("Zaeim rijd jullie naar jullie huis en jullie leven nog een rustige leven. [Einde 2]")
      space2()
      appEnding = 2
      if appEnding == 2:
          input("Typ [Enter] om de programma af te sluiten")
          exit()

#vraag 7.3 | als je naar het westen wilt reizen komt deze dialoog
if inputG == "naar het westen reizen" or inputG == "naar westen reizen" or inputG == "naar de westen reizen" or inputG == "naar westen gaan":
      space1()
      print("Jij besluit dat je naar Duitsland en Nederland wilt reizen")
      print("je zegt tegen Akram: “ik wil zo snel mogelijk naar het westen toe”")
      print("Hij antwoord: “nogmaals het gaat een maandje of 2 duren totdat we naar het westen kunnen reizen,")
      print("tot die tijd kunnen jullie hier even leven.")
      print("Zoek een huis zoek wat werk en maak er het beste van”")

space1()
#Deel 11
print("Deel 11")
space2()
print("Zaeim heeft een klein huisje voor jullie geregeld en heeft gezegd dat hij jullie naar naartoe wilt brengen met een auto.")
print("Jullie komen aan bij een klein huisje en hij geeft jullie 200 euro en een kleine oude Nokia telefoon.")
print("Hij zegt: “vind een goede baan en maak er het beste van, Akram belt je als jullie weg kunnen”")
space2()
print("2 maanden later....")

#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")

space1()

#Deel 12
print("Deel 12")
space2()
print("Na 2 maanden wordt je gebeld op je telefoontje en zegt Akram dat het tijd is dat jullie op reis kunnen.")
print("Jullie spreken af bij een winkel en hij zegt dat hij met een truck jouw naar Duitsland kan brengen.")
print("Jullie stappen in de achterkant van de truck en begint te rijden naar Duitsland. ")

#klik enter om door te gaan
space2()
input("Typ [Enter] om door te gaan")

#Deel 13
space1()
print("Deel 13")
space2()
print("5 uur later...")
space2()

#als een paar leden in slovakije blijven dan komt deze dialoog
if groepblijftinSlovakije == 1:
    print("Jij en de leden die er nog zijn zitten in de truck en jullie zijn bijna bij de grens.")

#als de groep met zijn allen naar Duitsland en Nederland willen reizen komt deze dialoog
if groepblijftinSlovakije == 2:
    print("Jij en de groep zitten in de truck en jullie zijn bijna bij de grens.")

print("Jullie komen aan bij de grens van Duitsland en Akram maakt snel een pitstop")
print("terwijl hij bezine pompt in de truck komt er een groep politie agenten naar hem toe en vragen hem wat er in de truck zit.")
print("Jullie worden aangehouden door de politie agenten en jullie worden naar een politie bureau gebracht.")
print("Ze hebben jullie identiteiten vast gelegd en ze zeggen dat je hier in Duitsland kan blijven of naar een ander land kan gaan")

space2()

#vraag 8
print("je krijgt hier de keuze om in Duitsland te blijven of naar Nederland te gaan" )
print("kies uit [Duitsland] of [Nederland]")

inputH = input()

if inputH == "Duitsland" or inputH == "duitsland" or inputH == "duistland":
    print("je zegt dat je hier in Duitsland wilt blijven")
    print("jij blijft hier en je regelt de documenten nodig om in duitsland te blijven")

if inputH == "Nederland" or inputH == "nederland":
    print("Jij zegt dat je naar Nederland wilt gaan")

    space2()
    #Deel 14

    print("Deel 14")
    space2()
    #Einde 3 en 4

    print("Je reist met de trein naar Nederland.")
    print("jij komt aan in Nederland en je gaat naar de politie en vraagt of hij kan blijven.")
    print("hij wordt geholpen en zijn asielprocedure begint.")
    print("hij mag uitrusten terwijl de overheid probeert te regelen dat jij hier kan blijven. [einde 4]")

space1()
print("Deel 15")


#als je in nederland leeft en Davie is dood dan komt deze dialoog | Einde 4
if inputH == "Nederland" and davielifeStatus == "dead" or inputH == "nederland" and davielifeStatus == "dead":
    print("je leeft nu in Nederland en je leeft met je zoon en jullie hebben een verblijfsvergunning gekregen")
    print("Jij krijgt een huis en je probeert na een paar dagen rust werk te zoeken.")
    print("je hebt na een paar weken een goede baan en jullie beginnen een nieuwe leven. ")
    appEnding = 2
    if appEnding == 2:
        input("Typ [Enter] om de programma af te sluiten")
        exit()

#als je in nederland leeft en Davie leeft nog dan komt deze dialoog | Einde 4
if inputH == "Nederland" and davielifeStatus == "alive" or inputH == "nederland" and davielifeStatus == "alive":
    print("je leeft nu in Nederland en je leeft met je zoon en vrouw en jullie hebben een verblijfsvergunning gekregen")
    print("je krijgt een huis en je probeert na een paar dagen rust werk te zoeken")
    print("je hebt na een paar weken een goede baan en jullie beginnen een nieuwe leven. ")
    appEnding = 2
    if appEnding == 2:
        input("Typ [Enter] om de programma af te sluiten")
        exit()

#als je in duitsland leeft en Davie leeft dan komt deze dialoog | Einde 3
if inputH == "Duitsland" and davielifeStatus == "alive" or inputH == "duitsland" and davielifeStatus == "alive":
    print("je leeft nu in Duitsland en je leeft met je zoon en vrouw en jullie hebben een verblijfsvergunning gekregen")
    print("je krijgt een huis en je probeert na een paar dagen rust werk te zoeken")
    print("je hebt na een paar weken een goede baan en jullie beginnen een nieuwe leven")
    appEnding = 2
    if appEnding == 2:
        input("Typ [Enter] om de programma af te sluiten")
        exit()


#als je in duitsland leeft en Davie is dood dan komt deze dialoog | Einde 3
if inputH == "duitsland" and davielifeStatus == "dead" or inputH == "Duitsland" and davielifeStatus == "dead":
    print("je leeft nu in Duitsland en je leeft met je zoon en jullie hebben een verblijfsvergunning gekregen")
    print("je krijgt een huis en je probeert na een paar dagen rust werk te zoeken")
    print("je hebt na een paar weken een goede baan en jullie beginnen een nieuwe leven")
    appEnding = 2
    if appEnding == 2:
        input("Typ [Enter] om de programma af te sluiten")
        exit()


