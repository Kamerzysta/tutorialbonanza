import random

def gjette_tall_spill():
    print("Velkommen til 'Gjett Tallet'-spillet!")
    print("Jeg tenker på et tall mellom 1 og 100. Kan du gjette hvilket?")

    # Generer et tilfeldig tall mellom 1 og 100
    hemmelig_tall = random.randint(1, 100)
    antall_forsøk = 0

    while True:
        try:
            gjett = int(input("Skriv inn ditt gjett: "))
            antall_forsøk += 1

            if gjett < hemmelig_tall:
                print("For lavt! Prøv igjen.")
            elif gjett > hemmelig_tall:
                print("For høyt! Prøv igjen.")
            else:
                print(f"Gratulerer! Du gjettet riktig på {antall_forsøk} forsøk.")
                break
        except ValueError:
            print("Vennligst skriv inn et gyldig tall.")

if __name__ == "__main__":
    gjette_tall_spill()