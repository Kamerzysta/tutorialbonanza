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