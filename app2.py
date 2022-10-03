#String -> text
#int -> geheel getal
#float -> komma getal
#boolean -> True of False

import math

x="5"
y=5
z=5.0

print("Syntra")
print(5)

def printLeeftijd(leeftijd):
    print(leeftijd)

leeftijd=int(input("leeftijd: "))

printLeeftijd(leeftijd)    

def oldEnoughToDrive(leeftijd):
    result=""
    if leeftijd>18:
        result="U bent oud genoeg om te rijden"
    else:
        result="U bent niet out genoeg om te rijden"

    print(result)

def calc_sqrt(getal):
    x= math.sqrt(getal)
    print(x)

def aantalKleinerDan5(getallen):
    kleinerDan5=0

    for i in getallen:
        if i<5:
            kleinerDan5+=1
    print(f"{kleinerDan5} getallen zijn kleiner dan 5")

getallen = [15,1,3,18,1,23,2,15,4,5]

aantalKleinerDan5(getallen)



