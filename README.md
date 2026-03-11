# 💣 Minesweeper

<p align="center">
  Classic Minesweeper game built with <b>Python</b> and <b>Pygame</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pygame-Game%20Development-2ecc71"/>
  <img src="https://img.shields.io/github/stars/akyy0707/MineSweeper?style=social"/>
</p>

---

## 📖 Overview

This project is a **Python implementation of the classic Minesweeper game** using the **Pygame** library.

Players uncover cells on a grid while avoiding hidden mines. Each revealed cell displays the number of mines in the surrounding area, helping players logically determine safe moves.

The project focuses on **grid-based algorithms, recursive cell revealing, and event-driven game logic**.

---

## 🎮 Gameplay

- The board contains hidden mines randomly placed across a grid  
- Revealing a safe cell shows the **number of nearby mines**  
- Cells with **0 neighboring mines automatically reveal adjacent cells**  
- Clicking a mine results in **game over**

🏆 The player wins by revealing **all non-mine cells**.

---

## ✨ Features

- Randomized mine placement  
- Grid-based board system  
- Neighbor mine calculation  
- Recursive flood-fill reveal  
- Flag system for marking mines  
- Win and lose detection  
- Interactive UI using Pygame  

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming |
| Pygame | Rendering and input handling |
| OOP | Game architecture |

---


---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/akyy0707/MineSweeper.git
cd MineSweeper
```
Install dependencies:
```bash
pip install pygame
```
Run the game:
```bash
python main.py
```
🎮 Controls
Action	Input
Reveal cell	Left Click
Flag mine	Right Click
🚀 Future Improvements

Difficulty levels

Timer system

Sound effects

UI improvements

👨‍💻 Author

Anh Tuấn

Anh Kỳ

Kiến Văn

Thanh Văn
