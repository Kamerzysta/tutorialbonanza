# Gjett Tallet: En Nettside-Tutorial

## Introduksjon

I denne tutorialen skal vi lage "Gjett Tallet"-spillet som en nettside! Spillet vil bruke **HTML**, **CSS**, og **JavaScript** for å gi brukerne en interaktiv opplevelse rett i nettleseren.

### Hva vil du lære?

- Hvordan lage en enkel nettside med HTML og CSS
- Hvordan bruke JavaScript for å implementere logikk
- Hvordan håndtere brukerinput og gi tilbakemeldinger

---

## Forarbeid

### Hva trenger vi?

1. **En nettleser**: For å kjøre nettsiden.
2. **En teksteditor**: Bruk Visual Studio Code, Sublime Text, eller Notepad++ for å skrive koden.

---

## Steg-for-steg

### Steg 1: HTML-struktur

Lag en ny fil og kall den `index.html`. Dette blir grunnstrukturen for nettsiden. Skriv følgende kode i filen:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Gjett Tallet</title>
  </head>
  <body>
    <h1>Gjett Tallet</h1>
    <p>Jeg tenker på et tall mellom 1 og 100. Kan du gjette hvilket?</p>

    <div id="game">
      <input type="number" id="guessInput" placeholder="Skriv inn ditt gjett" />
      <button onclick="makeGuess()">Gjett</button>
      <p id="result"></p>
    </div>
  </body>
</html>
```

Denne koden lager en grunnleggende nettside med et input-felt og en knapp for å gjette.

### Steg 2: Legg til CSS for styling

For å gjøre nettsiden penere, legg til en `<style>`-seksjon i `<head>`:

```html
<style>
  body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f4f4f9;
    color: #333;
    padding: 20px;
  }

  #game {
    margin-top: 20px;
    padding: 20px;
    border: 2px solid #ccc;
    border-radius: 10px;
    background-color: #fff;
    display: inline-block;
  }

  input[type="number"] {
    padding: 10px;
    margin: 10px 0;
    width: 50%;
  }

  button {
    padding: 10px 20px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  button:hover {
    background-color: #218838;
  }

  #result {
    margin-top: 20px;
    font-size: 1.2em;
  }
</style>
```

### Steg 3: Legg til JavaScript for logikk

For å få spillet til å fungere, legg til følgende `<script>`-seksjon rett før avsluttende `</body>`-taggen:

```html
<script>
  // Generer et tilfeldig tall mellom 1 og 100
  let secretNumber = Math.floor(Math.random() * 100) + 1;
  let attempts = 0;

  function makeGuess() {
    const guessInput = document.getElementById("guessInput");
    const result = document.getElementById("result");

    const guess = parseInt(guessInput.value);
    attempts++;

    if (isNaN(guess)) {
      result.textContent = "Vennligst skriv inn et gyldig tall!";
      return;
    }

    if (guess < secretNumber) {
      result.textContent = "For lavt! Prøv igjen.";
    } else if (guess > secretNumber) {
      result.textContent = "For høyt! Prøv igjen.";
    } else {
      result.textContent = `Gratulerer! Du gjettet riktig på ${attempts} forsøk.`;
      document.getElementById("guessInput").disabled = true;
    }

    guessInput.value = "";
  }
</script>
```

---
