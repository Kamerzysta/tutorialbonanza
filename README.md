# Gjett Tallet: En Python-Tutorial

## Introduksjon

I denne tutorialen skal vi lage et enkelt spill kalt **"Gjett Tallet"**. I spillet velger datamaskinen et tilfeldig tall mellom 1 og 100, og spilleren skal prøve å gjette hvilket tall det er. Etter hvert gjett får spilleren beskjed om tallet er for høyt, for lavt, eller riktig.

### Hva vil du lære?

- Hvordan generere tilfeldige tall i Python
- Bruk av `while`-løkker for gjentagende logikk
- Bruk av `try-except` for feilhåndtering
- Hvordan lese input fra brukeren

### Slik vil spillet fungere:

1. Datamaskinen velger et tilfeldig tall.
2. Spilleren gjetter tallet.
3. Programmet gir tilbakemelding (for høyt, for lavt, eller riktig).
4. Spillet fortsetter til spilleren gjetter riktig.

---

## Forarbeid

### Hva trenger vi?

1. **Python installert**: Last ned fra [python.org](https://www.python.org/) hvis du ikke har det.
2. **En kodeditor**: Du kan bruke IDLE, VS Code, PyCharm eller hvilken som helst annen teksteditor.
3. **Grunnleggende kunnskap**: Denne tutorialen er for nybegynnere, så du trenger bare minimal erfaring med Python.

---

## Steg-for-steg

### Steg 1: Oppsett av prosjekt

Lag en ny Python-fil, f.eks. `gjett_tallet.py`. Dette er filen hvor vi skal skrive koden vår.

### Steg 2: Importer nødvendige moduler

Vi bruker `random`-modulen for å generere tilfeldige tall. Legg til følgende linje øverst i filen din:

```python
import random
```

### Steg 3: Lag hovedfunksjonen

Opprett en funksjon som styrer spillets logikk. Skriv inn følgende kode:

```python
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
```

### Steg 4: Kjør spillet

Til slutt, legg til følgende kode nederst i filen for å starte spillet:

```python
if __name__ == "__main__":
    gjette_tall_spill()
```

---

## Feilsøking

Her er noen vanlige problemer du kan møte på:

1. **Input-feil**: Hvis spilleren skriver inn noe annet enn et tall, vil programmet krasje uten `try-except`-blokken. Sørg for å inkludere den!

2. **Uendelig løkke**: Hvis du glemmer å oppdatere `antall_forsøk` eller sjekke riktig betingelse, kan programmet havne i en evig løkke. Dobbeltsjekk `while True`-betingelsen.

3. **Tilfeldige tall**: Hvis det hemmelige tallet alltid er det samme, har du kanskje glemt å bruke `random.randint()` riktig.

---
