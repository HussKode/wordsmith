# 🟩 Wordle (Terminal Version)

A simple terminal-based Wordle clone built in Python. The player has 6 attempts to guess a hidden 5-letter word, receiving color-coded feedback after each guess.

This project was built to practice Python fundamentals such as loops, conditionals, file handling, and basic game logic.

---

## 🎮 How It Works

- A random 5-letter word is selected from a word list.
- The player has **6 attempts** to guess the word.
- After each guess, feedback is shown:
  - 🟩 Green: Correct letter in the correct position
  - 🟨 Yellow: Correct letter in the wrong position
  - ⬜ Default: Letter not in the word
- The game continues until the word is guessed or attempts run out.

---

## 🧠 Features

- Random word selection from external dictionary files
- Input validation (must be a valid 5-letter word)
- Color-coded feedback in the terminal
- Play-again loop for continuous gameplay
- Clean command-line interface

---

## 📂 Project Structure


wordle-clone/
│
├── wordle.py # Game logic
├── guesses.txt # List of valid guess words
├── answers.txt # List of possible secret words
└── README.md


---

## 🛠️ Built With

- Python 3
- Standard Library (`random`, file handling)

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/HussKode/wordle-clone.git
```

2. Navigate into the project folder:
```bash
cd wordle-clone
```

3. Run the game:
```bash
python wordle.py
```

---

## 📌 What I Learned

This project helped me improve my understanding of:
- Python loops and conditionals
- File reading and data processing
- String manipulation
- Basic game logic design
- Command-line user interaction

---

## 🔮 Possible Improvements

- Add win/loss statistics tracking
- Improve letter evaluation logic (handle duplicate letters more accurately)
- Add difficulty modes (different word lengths)
- Improve terminal UI formatting
- Add a hint system



## 👨‍💻 Author

Built as a personal Python project to practice programming fundamentals and game development logic.
```

