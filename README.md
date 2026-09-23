# TURTLE-racing-game
Explore some secret built in module in python : >

# 🐢 Turtle Race Betting Game

A simple, interactive 2D turtle racing game built using Python's native **Turtle Graphics** library. Players place a bet on which colored turtle will win the race before the simulation begins.

## 🎮 How to Play

1. **Launch the game:** A 1920x1080 black window will appear with 6 differently colored turtles lined up at the starting line.
2. **Make your guess:** A pop-up box will prompt you to enter your guess.
3. **Enter a color:** Type one of the available turtle colors: `red`, `green`, `blue`, `yellow`, `orange`, or `purple`.
4. **Watch the race:** The turtles will move forward at random speeds.
5. **Check the result:** The game console will announce the winner and tell you if your guess was correct.

## 🛠️ Prerequisites & Installation

This game relies entirely on standard Python libraries. No external packages are required.

1. **Python 3.x** must be installed on your system.
2. Clone or download the game script (e.g., `main.py`).

## 🚀 Running the Game

Open your terminal or command prompt, navigate to the folder containing the script, and run:

```bash
python main.py
```

## 📝 Code Overview

* **Graphics:** Uses the `turtle.Screen` module to set up a full-HD dark mode environment.
* **Game Loop:** A `while` loop continuously moves the turtles forward by a random integer between `0` and `20` pixels per frame.
* **Win Condition:** The first turtle to cross the x-coordinate boundary of `645` stops the race and is declared the winner.
