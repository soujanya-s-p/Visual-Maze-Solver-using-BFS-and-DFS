# 🧩 Visual Maze Solver using BFS & DFS

A complete Python-based maze-solving visualizer using **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.  
This project includes static mazes, dynamic mazes, custom maze input, animation, and side-by-side comparison of BFS vs DFS.

---

## 📌 Overview

This project helps you understand how BFS and DFS explore a maze differently:

- **BFS → Always finds the shortest path**
- **DFS → May find a path, but not guaranteed shortest**
- **Animated visualization** shows algorithm behaviour step-by-step.

You can load:
- Predefined mazes  
- Random mazes  
- Interactive user-generated mazes  

---

## 📁 Project Structure

```bash
│
├── maze20x20.py # Solves a predefined 20×20 maze
├── mazesolver.py # Simple BFS & DFS example
├── newmaze.py # Animated BFS/DFS solver with visited visualization
├── visualmaze.py # User-input maze creator and solver
└── README.md
```

---

## 🚀 Features

### ✔ BFS Implementation
- Finds shortest path  
- Uses queue  
- Tracks visited nodes  
- Can animate visited cells + final path  

### ✔ DFS Implementation
- Uses recursion / stack  
- Explores deep paths first  
- Helps compare behaviour with BFS  

### ✔ Visualization
- Console visualization  
- Color-coded path + visited nodes  
- Optional animation speed control  

### ✔ Interactive Maze
- Enter rows/columns  
- Enter each row manually  
- Useful for testing custom patterns  

---

## 🧠 Algorithms Explained

### **1. Breadth-First Search (BFS)**  
BFS expands level-by-level.  
Perfect for shortest paths in grids.

Steps:
1. Add start to queue  
2. Pop → Explore neighbors  
3. Mark visited  
4. Stop when goal reached  
5. Backtrack using parent dictionary to build final path  

---

### **2. Depth-First Search (DFS)**  
DFS explores deep in one direction before checking others.

Steps:
1. Start recursion at start cell  
2. Move through valid neighbors  
3. Backtrack on dead ends  
4. Stop when goal found  

DFS does **not** guarantee shortest path.

---

## ▶️ How to Run the Programs

### Run the 20×20 maze solver
```bash
python maze20x20.py
```
### Create + solve your own maze
```bash
python visualmaze.py
```
## Contributors
1. Soujanya S P
2. Kushi M Yarnal


