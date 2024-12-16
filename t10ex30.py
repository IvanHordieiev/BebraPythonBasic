import time
import random

def intro():
    print("En una època on els gegants governen Menorca. Nosaltres necessitem menjar,\n"
          "Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.\n"
          "Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran\n"
          "i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.\n")

def canvi_talaiot():
    talaiot = ""
    while talaiot not in ["1", "2"]:
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

def trobada(canvi_talaiot):
    print("T'estas apropant al talaiot...")
    time.sleep(2)
    print("Està fosc i és tenebrós...")
    time.sleep(2)
    print("Un gran gegant salta davant teu, t'agafa i ...\n")
    time.sleep(2)

    gegantamic = random.randint(1, 2)
    if canvi_talaiot == str(gegantamic):
        print("Et convida a menjar...\n")
        return True 
    else:
        print("Se't menja d'un mos...\nÑAMÑAMÑAM\n")
        return False  

def main():
    partida_nova = "si"
    punts = 0

    while partida_nova in ["s", "si"]:
        intro()
        n_talaiot = canvi_talaiot()
        if trobada(n_talaiot):
            punts += 1  
        else:
            break  
        partida_nova = input("Vols tornar a jugar? Introdueixi si o no: ").lower()
        print()

    print(f"Has aconseguit {punts} punts.")

if __name__ == "__main__":
    main()
