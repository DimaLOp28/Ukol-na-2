while True:
#Ukol A(Sofiia)
  
    jidlo1 = input("Zadej první jídlo: ")
    kalorie1 = int(input(f"Kolik kalorií má {jidlo1}? "))
 
    jidlo2 = input("Zadej druhé jídlo: ")
    kalorie2 = int(input(f"Kolik kalorií má {jidlo2}? "))
 
    jidlo3 = input("Zadej třetí jídlo: ")
    kalorie3 = int(input(f"Kolik kalorií má {jidlo3}? "))
 
    celkoveKalorie = kalorie1 + kalorie2 + kalorie3
    print(f"Celkový počet kalorií za den: {celkoveKalorie}")
 
 
#Ukol B(Diana)
    aktivita1=str(input("Jakou aktivitu jste dělali? "))
    aktivita2=str(input("Jakou druhou aktivitu jste dělali? "))
    delka1=int(input("Jaká je délka první aktivity? V minutách: "))
    delka2=int(input("Jaká je délka druhý aktivity? V minutách: "))
 
    kcal1=delka1*5
    kcal2=delka2*5
    print("Celkový počet kalorie je: ", kcal1+kcal2)
 
#Společný
    snedl=celkoveKalorie
    spalil=kcal1+kcal2
    if(snedl-spalil>0):
        print("Máte přebytek kalorie")
    elif(snedl-spalil<0):
        print("Máte nedostatek kalorie")
    else:
        print()
  
    pokracovat = input("Chcete zadat další den? (ano/ne): ").strip().lower()
    if pokracovat != "ano":
        break
