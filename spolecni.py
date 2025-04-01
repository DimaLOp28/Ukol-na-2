#Zadání aktivit
 
aktivita1 = input("Jakou aktivitu jste dělali? ") 
aktivita2 = input("Jakou druhou aktivitu jste dělali? ") 
delka1 = int(input("Jaká je délka první aktivity? V minutách: ")) 
delka2 = int(input("Jaká je délka druhé aktivity? V minutách: "))
 
#Výpočet spálených kalorií
 
kcal1 = delka1 * 5 
kcal2 = delka2 * 5 
celkove_spalene = kcal1 + kcal2
 
#Zadání jídel a jejich kalorických hodnot
 
jidlo1 = input("Zadej první jídlo: ") 
kalorie1 = int(input(f"Kolik kalorií má {jidlo1}? ")) 
jidlo2 = input("Zadej druhé jídlo: ") 
kalorie2 = int(input(f"Kolik kalorií má {jidlo2}? ")) 
jidlo3 = input("Zadej třetí jídlo: ") 
kalorie3 = int(input(f"Kolik kalorií má {jidlo3}? "))
 
#Výpočet celkových kalorií
 
celkove_kalorie = kalorie1 + kalorie2 + kalorie3
 
#Výpočet bilance
 
bilance = celkove_kalorie - celkove_spalene
 
#Výpis výsledků
 
print(f"Snedl/a jsi {celkove_kalorie:.1f} kcal a spálil/a {celkove_spalene:.1f} kcal.") 
print(f"Bilance: {bilance:.1f} kcal") 
if bilance > 0: print(f"Přebýtek: {bilance:.1f} kcal") 
elif bilance < 0: print(f"Nedostatek: {-bilance:.1f} kcal") 
else: print("Přesná rovnováha kalorií.")