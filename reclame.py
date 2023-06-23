from algemene_functies import mijn_functie_2

def aanbiedingen_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs*korting)
    print (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro")
aanbiedingen_1 ("aarbei",4,0.1)

def inkomsten_totaal(inkomsten,btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.")
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09 
print (inkomsten_totaal(inkomsten_per_dag, btw_percentage))

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return (hoogste, laagste)
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten_per_dag)
print (resultaat)

def gemiddelde (mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal_waarden = len(mijn_lijst)
    gemiddelde_inkomsten = totaal / aantal_waarden
    return (f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro")
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
uitkomst = gemiddelde(inkomsten_per_dag)
print (uitkomst)

def meervoudig (invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return (resultaat)
cijfers = [10, 5, 3, 2, 1, 2, 9]
uitkomst = meervoudig(cijfers)
print (uitkomst)

def combinatie (invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return (uitvoer)

