jidlo1 = input("Zadej první jídlo: ")
kalorie1 = int(input(f"Kolik kalorií má {jidlo1}? "))
 
jidlo2 = input("Zadej druhé jídlo: ")
kalorie2 = int(input(f"Kolik kalorií má {jidlo2}? "))
 
jidlo3 = input("Zadej třetí jídlo: ")
kalorie3 = int(input(f"Kolik kalorií má {jidlo3}? "))

celkove_kalorie = kalorie1 + kalorie2 + kalorie3
print(f"Celkový počet kalorií za den: {celkove_kalorie}")